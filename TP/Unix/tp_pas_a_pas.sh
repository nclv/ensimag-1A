#!/bin/bash

# création 5 répertoires.
for i in $(seq 5)
do
    # test de l'existence du répertoire à créer.
    if [ ! -d "dir$i" ]
    then
        mkdir "dir$i"
    fi
    # création de 5 fichiers dans chaque répertoire créé.
    # le mois de création des fichiers est compris entre janvier et mai.
    for j in $(seq 5)
    do
        echo "Contenu pas bien important ..." > "dir$i/file$j.txt"
        touch -d "2013/$j/01" "dir$i/file$j.txt"
    done
done
 
echo "C'est fini ! Tappez ls pour voir les répertoires créés."
