echo "Введіть число"
read num
if [ $num -gt 10 ];
then
echo "Число > 10"
elif [ $num -eq 10 ];
then
echo "Число = 10"
elif [ $num -lt 10 ];
then
echo "Число < 10"
else
echo "Некоректне число"
fi