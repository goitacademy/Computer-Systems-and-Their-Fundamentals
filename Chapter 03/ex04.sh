#оголошуємо змінну
var=7
#використовуємо оператор OR в if-умові
if [[ ( $var -gt 5 ) || ( $var -eq 7 ) ]]
then
echo "$var >5 або =7"
else
echo "$var не >5 і не =7"
fi