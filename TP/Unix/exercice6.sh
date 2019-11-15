#! /bin/sh

# Attention aux espaces !
if [ "$1" -gt "$2" ]; then
    echo "Le nombre $1 est superieur au nombre $2"
elif [ "$1" -lt "$2" ]; then
    echo "Le nombre $1 est inferieur au nombre $2"
else
    echo "Le nombre $1 est egal au nombre $2"
fi

