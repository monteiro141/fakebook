python3 main.py < Fakebook-Tests-20-Dez/fakebook00in.txt > oo0
python3 main.py < Fakebook-Tests-20-Dez/fakebook01in.txt > oo1
python3 main.py < Fakebook-Tests-20-Dez/fakebook03in.txt > oo3
python3 main.py < Fakebook-Tests-20-Dez/fakebook02in.txt > oo2
python3 main.py < Fakebook-Tests-20-Dez/fakebook04in.txt > oo4
python3 main.py < Fakebook-Tests-20-Dez/fakebook05in.txt > oo5
python3 main.py < Fakebook-Tests-20-Dez/fakebook06in.txt > oo6
python3 main.py < Fakebook-Tests-20-Dez/fakebook07in.txt > oo7
python3 main.py < Fakebook-Tests-20-Dez/fakebook08in.txt > oo8
python3 main.py < Fakebook-Tests-20-Dez/fakebook09in.txt > oo9
python3 main.py < Fakebook-Tests-20-Dez/fakebook10in.txt > oo10
python3 main.py < Fakebook-Tests-20-Dez/fakebook11in.txt > oo11
python3 main.py < Fakebook-Tests-20-Dez/fakebook12in.txt > oo12
python3 main.py < Fakebook-Tests-20-Dez/fakebook13in.txt > oo13
python3 main.py < Fakebook-Tests-20-Dez/fakebook14in.txt > oo14
python3 main.py < Fakebook-Tests-20-Dez/fakebook15in.txt > oo15


diff oo0 Fakebook-Tests-20-Dez/fakebook00out.txt > dif0
diff oo1 Fakebook-Tests-20-Dez/fakebook01out.txt > dif1
diff oo2 Fakebook-Tests-20-Dez/fakebook02out.txt > dif2
diff oo3 Fakebook-Tests-20-Dez/fakebook03out.txt > dif3
diff oo4 Fakebook-Tests-20-Dez/fakebook04out.txt > dif4
diff oo5 Fakebook-Tests-20-Dez/fakebook05out.txt > dif5
diff oo6 Fakebook-Tests-20-Dez/fakebook06out.txt > dif6
diff oo7 Fakebook-Tests-20-Dez/fakebook07out.txt > dif7
diff oo8 Fakebook-Tests-20-Dez/fakebook08out.txt > dif8
diff oo9 Fakebook-Tests-20-Dez/fakebook09out.txt > dif9
diff oo10 Fakebook-Tests-20-Dez/fakebook10out.txt > dif10
diff oo11 Fakebook-Tests-20-Dez/fakebook11out.txt > dif11
diff oo12 Fakebook-Tests-20-Dez/fakebook12out.txt > dif12
diff oo13 Fakebook-Tests-20-Dez/fakebook13out.txt > dif13
diff oo14 Fakebook-Tests-20-Dez/fakebook14out.txt > dif14
diff oo15 Fakebook-Tests-20-Dez/fakebook15out.txt > dif15

for i in {0..15}
do
    if [ -s dif$i ]; then 
    echo "dif$i"
    else
    rm dif$i
    rm oo$i
    fi
done


