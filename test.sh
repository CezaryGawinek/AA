#!/bin/bash
#chmod +x test.sh
#./test.sh
# echo "Jak masz na imie?"
# read imie 
# echo "Cześć, $imie!"

# echo "Podaj liczbę"
# read liczba
# if [ $liczba -gt 10 ]
# then 
#     echo "liczba jest większa od 10"
# else
#     echo "Licza jest mniesza od 10"
# fi

# for i in {1..20}
# do
#     echo "Iteracja $i"
# done

for(( i=1; i -ls $liczba ; i++ ))
do
    echo "Iteracja $i"
done