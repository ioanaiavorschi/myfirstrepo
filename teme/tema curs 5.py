#1
def suma(a,b):
    return a+b
print(suma(7,8))

#2
def par_impar(a):
    if a%2==0:
        return True
    else:
        return False
print(par_impar(8))

#3
def nr_caractere(a):
    return len(a)
print(nr_caractere('Ioana Iavorschi'))


#4 aria dreptunghiului
def aria_dreptunghiului(L,l):
    return L*l
print(aria_dreptunghiului(9,6))

#5 aria cercului
def pi_value():
    return 3.14
def aria_cercului(r):
    return pi_value()*r*r
print(aria_cercului(6))

#6
def gaseste_x(cuvant):
    if 'x' in cuvant:
        return True
    else:
        return False
print(gaseste_x('extemporal'))

#7
def lit_mari_mici(cuvant):
    print(f'Numarul de caractere mici este', sum([int(c.islower()) for c in cuvant]))
    print(f'Numarul de caractere mari este', sum([int(c.isupper()) for c in cuvant]))

lit_mari_mici('XLab')

#8
def l_num_poz(numere):
    l_num_poz = []
    for numar in numere:
        if numar >0:
            l_num_poz.append(numar)
    return l_num_poz
print(l_num_poz([50,-96,9,-5,-2,67]))

#9
def verif_numere(x,y):
    if x > y:
        print(f'{x} este mai mare decat {y}')
    elif y > x:
        print(f'{y} este mai mare decat {x}')
    else:
        print('numerele sunt egale')

verif_numere(45,77)

#10
def nr_in_set(a,set):
    set = {}
    if a in set:
        print('Nu am adaugat numarul nou in set, acesta exista deja')
        return False
    else:
        print('Am adaugat numarul in set')
        return True
nr_in_set(3,{3,5,7})





        




