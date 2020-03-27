#!/usr/bin/env bash

: '
VINCENT Nicolas

Utilisation de cProfile pour créer un fichier .prof puis affichage du fichier avec snakeviz.

USAGE:
  bash performances.sh perf.prof pyhack.py
'

echo $(python3 --version)

# fichier .py
input_file=$1;
# fichier .prof
output_file=$2;

python3 -m pip install snakeviz

if [[ ( $input_file == *.py ) && ( $output_file == *.prof ) ]]; then
  python3 -m cProfile -o $output_file $input_file
  python3 -m snakeviz $output_file
else
  echo "Les extensions des fichiers ne sont pas valides"
fi
