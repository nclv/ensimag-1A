#! /bin/sh

for fichier in ALL/*.txt
do
    if [ -f "$fichier" ]; then
	# ls -l affiche la date, mais d'une manière peu pratique à
	# utiliser dans un script (dans la vraie vie, c'est une très
	# mauvaise idée d'utiliser la sortie de ls -l dans un script).
	# stat fait à peu près la même chose, mais est beaucoup plus
	# pratique/fiable à utiliser dans un script.
	date=$(stat --format='%y' ALL/fichier1.txt)
	echo "$date"
	joliedate=$(date -d "$date")
	echo "Fichier soi-disant créé le $joliedate" >> $fichier
    fi
done
