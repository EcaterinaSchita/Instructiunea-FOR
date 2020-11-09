n=eval(input('introdu numarul'))
suma=0
for x in range (1, n+1):
    if ((x%3==0) and (x%5==0)):
        suma=suma+x
        print('suma numerelor divizibile la 3 si 5 este ' , suma )