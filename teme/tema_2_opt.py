#1
x = int(input('introduceti un numar'))
y = len(str(x))
if y >= 4:
    print('numarul introdus are minim 4 cifre ')
else:
    print('numarul introdus nu are minim 4 cifre')

#2
if y ==6:
    print('numarul are 6 cifre')
else:
    print('numarul nu are 6 caractere')

#3
if x % 2 == 0:
    print('numarul este par')
else:
    print('numarul este impar')

#4
x = int(input('introduceti un numar'))
y = int(input('introduceti al doilea numar, diferit de primul'))
z = int(input('introduceti al treilea numar, diferit de primele doua'))
if x > y and x > z:
    print('primul numar este mai mare')
elif y > x and y > z:
    print('al doilea numar este mai mare')
else:
    print('al trelea numar este mai mare')

#5
x = input('introduceti valoarea primului unghi al triunghiului')
y = input('introduceti valoarea celui de al doilea unghi al triunghiului')
z = input('introduceti valoarea celui de al treilea unghi al triunghiului')
if int(x)+ int(y) + int(z) ==180:
    print('valorile introduse sunt valide pentru un triunghi')
else:
    print('valorile introduse nu sunt valide pentru un triunghi')








