# #!/bin/bash
# if [ "$1" == "plik" ]; then
#     touch "$2"
#     echo "Utwórz plik $2"
# elif [ "$1"== "katalog" ]; then
#     mkdir "${2:-"plik.txt"}"
#     echo "Utworzono katalog $2."
# else
#     echo "Nieznana akcja."
# fi

# for arg in "$@"; do
#     echo "Argument: $arg"
# done

for (( i=$#; i>0; i--)); do
    echo "Argument $i"
done