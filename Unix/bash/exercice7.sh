#! /bin/sh

# Lister tout les dossiers du repertoire courant
for n in *; do
    if [ -d "$n" ]; then
	echo "$n"
    fi
done

# find [0-9a-zA-Z]* -maxdepth 0 -type d
