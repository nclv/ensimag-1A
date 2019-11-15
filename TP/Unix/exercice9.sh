#! /bin/sh

# Lister tout les dossiers du repertoire donne en argument
# et tester si l'argument est un repertoire valide

if [ -d "$1" ]; then
    (
	cd "$1"
	for n in *; do
	    if [ -d "$n" ]; then
		echo "$n"
	    fi
	done
    )
else
    echo "$1 n'est pas un repertoire valide."
fi

