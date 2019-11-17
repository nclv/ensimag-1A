#! /bin/sh

# supprimer les espaces dans les noms de fichiers; 
# renommer si le nom existe deja

# creer des fichiers pour tester
echo "blabla" > "un nom avec espaces"
echo "blabla" > "un autre nom avec espaces"
echo "blabla" > "unnomavecespaces"
echo "blabla" > "unnomavecespaces1"
#

c=0
for f in *; do
    if [ -f "$f" ]; then
	nom=`echo "$f" | sed 's/ //g'`
	# tester si le nom $f a des espaces
	if [ "$f" != "$nom" ]; then
	    if [ -e "$nom" ]; then
		c=1;
		while [ -e "$nom$c" ]; do
		    c=$(($c + 1))
		done
		nom=$nom$c
	    fi
	    echo "$f" '->' "$nom"
	    mv "$f" "$nom"
	fi
    fi
done
