python3 main.py < Fakebook-Tests-20-Dez/fakebook09in.txt > oo0

diff oo0 Fakebook-Tests-20-Dez/fakebook09out.txt > dif0

for i in {0..0}
do
    if [ -s dif$i ]; then 
    echo "dif$i"
    else
    rm dif$i
    rm oo$i
    fi
done