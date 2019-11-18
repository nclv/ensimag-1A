#! /bin/sh

# Lister tout les dossiers du repertoire donne en argument

# les parentheses font que le changements de repertoire
# sont defaits a la fin (sous-shell)
(
    cd "$1"
    for n in *; do
	# echo "testing:$n"
	if [ -d "$n" ]; then
	    echo "$n"
	fi
    done
)

# find Directory/[0-9a-zA-Z]* -maxdepth 0 -type d
