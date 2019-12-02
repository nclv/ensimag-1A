
# TODO: correspondance entre les termes anglais et ceux français (surtout au niveau du DNS)

 * ping -c 1 website.com
 * protocole ICMP, network layer (3), Ethernet II / Internet Protocol Version 4 / Internet Control Message Protocol frame, filtre icmp, 2 packets : Echo (ping sends an alphabet sequence during ping requests) request (type 8) and Echo (ping echoes the request sequence) reply (type 0)

 * telnet website.com 80

 * wget or curl website.com/dir_to/webpage.html
 * protocoles TCP/HTTP, filtre ip.addr == <ip_dest in HTTP GET packet>, packets : three way handshake (SYN, SYN/ACK ACK), HTTP GET, multiples ACK, FIN ACK, ACK
 First packet (SYN): Ethernet II (destination is your default gateway's MAC address, check with arp -a and source is your MAC address, check with ifconfig)/ Internet Protocol Version 4 (destination address is the IP address of the HTTP server and source address is your IP address)/ Transmission Control Protocol frame (destination port is http, source port is a dynamic port selected for this HTTP connection), all of the packets for this connection will have matching MAC addresses, IP addresses, and port numbers.
 Fourth packet (GET request): Ethernet II / Internet Protocol Version 4 / Transmission Control Protocol / Hypertext Transfer Protocol frame (GET request, Host, Connection, User-Agent, Referrer, Accept, and Cookie are the information passed to the HTTP server with the GET request)
 Fifth packet (TCP ACK): TCP acknowledgement of receiving the GET request.

 * The loopback networking interface is a virtual network device implemented entirely in software. All traffic sent to it "loops back" and just targets services on your local machine.

 * route -n : flags UG (Up and Gateway), ip route, netstat -rn to get its IP address
 arp -a to get its MAC address

 * use host (-t a/mx/ns/cname/soa/any, -6, -v) or dig (@{ns1.example.com} {example.com} {TYPE}, -x, +short) <website.com> for DNS lookup (IPv4 and IPv6 addresses, serveur de nom faisant autorité sur le domaine), nslookup -type=soa afnic.fr

 * Il est possible d'héberger plusieurs sites sur le même serveur.
 /etc/apache2/sites-available/monsite.conf
 <VirtualHost \*:80>
        ServerName monsite.fr
        ServerAlias monsite.com

        ServerAdmin webmaster@monsite.fr
        DocumentRoot /var/www/monsite

        LogLevel info
        ErrorLog ${APACHE_LOG_DIR}/monsite_error.log
        CustomLog ${APACHE_LOG_DIR}/monsite_access.log combined
 </VirtualHost>
 si une requête arrivant sur n’importe quel IP et sur le port 80 avec en valeur de Host: monsite.fr ou monsite.com alors il lui faut servir les fichiers se trouvant dans /var/www/monsite. Ensuite nous lui demandons de nous enregistrer les logs dans des fichiers spécifique au site et non dans les fichiers de log apache standard.
 a2ensite monsite.conf
 service apache2 reload

 * Un certificat de sécurité SSL permet de chiffrer les données échangées sur un site internet. Aucune information ne peut être interceptée. SSL certificate creation/expiration dates : echo | openssl s_client -servername www.renater.fr -connect www.renater.fr:443 2>/dev/null | openssl x509 -noout -dates (-issuer, -subject, -fingerprint) or whois <website.com>

 * Basic Access Authentification : The BA mechanism provides no confidentiality protection for the transmitted credentials. They are merely encoded with Base64 in transit, but not encrypted or hashed in any way. Therefore, Basic Authentication is typically used in conjunction with HTTPS/TLS to provide confidentiality.
 Because the BA field has to be sent in the header of each HTTP request, the web browser needs to cache credentials for a reasonable period of time to avoid constantly prompting the user for their username and password. Caching policy differs between browsers.
 HTTP does not provide a method for a web server to instruct the client to "log out" the user. However, there are a number of methods to clear cached credentials in certain web browsers.

 *
