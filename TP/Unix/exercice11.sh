#! /bin/sh

# deplacer les fichiers dans dir* vers le repertoire ALL
# et renommer; effacer les repertoires dir*

# si ALL n'existe pas, le creer
mkdir -p ALL

for d in dir*; do
    if [ -d "$d" ]; then
	(
	    cd "$d"
	    for f in *; do
		echo deplacant "$d/$f" vers "../ALL/$d-$f"
		if [ -f "$f" ]; then
		    mv "$f" "../ALL/$d-$f"
		fi
	    done
	)
	rmdir $d
    fi
done


