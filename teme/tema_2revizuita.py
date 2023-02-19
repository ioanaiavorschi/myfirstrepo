#1 un if else separa intr-o schema logica cum va curge codul

#2 verifica si afiseaza daca x este numar natural
'''x = int(input('introduceti un numar'))
if x >=0:
    print('numarul introdus este un numar natural')
else:
    print('numarul introdus nu este un numar natural')

#3 verifica si afiseaza daca x este un numar pozitiv, negativ sau neutru
x = int(input('intruduceti un numar'))
if x > 0:
    print('numarul introdus este pozitiv')
elif x==0:
    print('numarul introdus este neutru')
else:
    print('numarul introdus etse negativ')

#4 verifica si afiseaza daca x este intre -2 si 13
x = int(input('introduceti un numar'))
if x>-2 and x<13:
    print('numarul introdus este cuprins in intervalul -2  13')
else:
    print('numarul introdus nu este cuprins in intervalul -2  13')

#5 verifica si afiseaza daca diferenta dintre x si y etse mai mica de 5
x = int(input('introduceti un numar'))
y = int(input('introduceti un al doilea numar'))
if (x-y)<5:
    print('diferenta dintre cele 2 numere este mai mica decat 5')
elif (x-y)==5:
    print('diferenta dintre cele doua numere este 5')
else:
    print('diferenta dintre cele 2 numere nu este 5')

#6 verifica daca x nu este intre 5 si 27 (not)
x = int(input('introduceti un numar'))
if not(x>5 and x<27):
    print('x nu este cuprins intre 5 si 27')
else:
    print('x este cuprins intre 5 si 27')

#7 x si y int. verifica si afiseaza daca sunt egale, daca nu, afiseaza care dintre este mai mare.
x = int(input('intrudceti un numar'))
y = int(input('introduceti un al doilea numar'))
if x==y:
    print('cele doua numere sunt egale')
elif x>y:
    print('primul numar este mai mare decat al doilea')
else:
    print('al doilea numar este mai mare')'''

#8 x, y, z laturile unui triunghi, afiseaza daca triunghiul este isoscel, echilateral sau oarecare
'''x = int(input('introduceti dimenasiunea laturei x'))
y = int(input('introduceti dimenasiunea laturei y'))
z = int(input('introduceti dimenasiunea laturei z'))
if x==y==z:
    print('triunghiul este echilateral')
elif x==y and not(y==z) or y==z and not x==y or x==z and not y == x:
    print('triunghiul este isoscel')
else:
    print('triunghiul este unul oarecare')'''

#9 citeste o litera de la tastatura, verifica daca este vocala
o_litera = input('introduceti o litera')
if o_litera == 'a' or o_litera == 'e' or o_litera == 'i' or o_litera == 'o' or o_litera == 'u':
    print('litera introdusa este o vocala')
else:
    print('litera introdusa este o consoana')

#10
nota = float(input('introduceti nota'))
if nota >= 9:
    print('noua ta nota este A')
elif nota >= 8 and nota < 9:
    print('noua ta nota este B')
elif nota >=7 and nota < 8:
    print('noua ta nota este C')
elif nota >= 6 and nota < 7:
    print('noua ta nota este D')
elif nota > 4 and nota < 6:
    print('noua ta nota este E')
else:
    print('noua ta nota este F')


