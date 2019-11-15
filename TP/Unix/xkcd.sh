#! /bin/sh

# Si on veut une version lisible, on peut écrire :
for i in $(seq 1 3)
do
    wget "$(wget -O - http://xkcd.com/$i | grep hotlink | grep -o 'http.*jpg')" \
	-O $(printf "%03d" $i).jpg
done

# ... mais l'énoncé précisait "en une ligne" (ce qui est bien pratique
# quand on exécute la ligne interactivement dans un terminal plutôt
# que dans un script), donc on peut bien sûr écrire :
#
# for i in `seq 1 3` ; do wget "`wget -O - http://xkcd.com/$i | grep hotlink | grep -o http.\*jpg`" -O `printf "%03d" $i`.jpg ; done
# 
# ou bien, si on préfère les pipes aux backquotes :
#
# for i in $(seq 1 3); do wget -O - http://xkcd.com/$i | grep hotlink | grep -o 'http://.*\.jpg' | xargs wget -O $(printf %03d $i).jpg; done
