

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
