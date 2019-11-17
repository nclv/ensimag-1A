#! /bin/sh

# Ajouter a tout les fichiers classes dans
# ALL la date de la derniere modification

for f in ALL/*; do
    if [ -f "$f" ]; then
	date=`ls -l $f | sed 's/^[^ ]* *[^ ]* *[^ ]* *[^ ]* *[^ ]* *\([^ ]* *[^ ]* *[^ ]*\) .*/\1/'`
	echo "$f" "->" "$date"
	echo "$date" >> "$f"
    fi
done
