#!/bin/bash
#оголошуємо змінну
var=1
while [ $var -le 10 ]
do
echo "Значення змінної var =  $var"
#збільшуємо значення змінної на 1
(( var++ ))
done