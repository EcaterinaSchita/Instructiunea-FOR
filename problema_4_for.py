a=eval(input('introdu primul numar'))
b=eval(input('intrudo cel de al doilea numar'))
for x in range (a, b+1, 2):
    if(x%2!=0):
        print(x, end='')
       