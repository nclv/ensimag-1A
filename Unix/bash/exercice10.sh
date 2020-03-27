#! /bin/sh

# Lister tout les dossiers de plusieurs repertoires
# donne en argument
# et tester si les arguments sont des repertoires valides

for dossier in "$@"; do
    echo "Listing des sous-dossiers de $dossier ..."
    if [ -d "$dossier" ]; then
	(
	    cd "$dossier"
	    for n in *; do
		if [ -d "$n" ]; then
		    echo "$n"
		fi
	    done
	)
    else
	echo "$dossier n'est pas un repertoire valide."
    fi
done
