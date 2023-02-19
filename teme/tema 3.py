#1
note_muzicale = ['do','re','mi','fa','sol','la','si','do']
print(note_muzicale)
print(note_muzicale[::-1])
note_muzicale.reverse()
print(note_muzicale)

#2
note_muzicale = ['do','re','mi','fa','sol','la','si','do']
print(note_muzicale.count('do'))

#3-1
lista_1 = [3,1,0,2]
lista_2 = [6,5,4]
lista = lista_1 + lista_2
print(lista)

#3-2
lista_1 = [3,1,0,2]
lista_2 = [6,5,4]

lista_1.extend(lista_2)
print(lista_1)
#4
lista = [3,1,0,2,6,5,4]
lista.sort()
print(lista)

lista.remove(0)
print(lista)

#5
lista = [3,1,0,2,6,5,4]
if lista == 0:
    print('lista este goala')
else:
    print('lista nu este goala')
#6
lista = [3,1,0,2,6,5,4]
lista.clear()
print(lista)

#7
if lista == 0:
    print('lista este goala')
else:
    print('lista nu este goala')

#8
dict1 = {
    'Ana':8,
    'Gigel':10,
    'Dorel':5,
}
elevii = dict1.keys()
print(elevii)

#9

x = dict1.items()
print("notele elevilor sunt:", x)

#10
dict1['Dorel'] = 6
print(dict1)

#11
dict1.pop('Gigel')
dict1['Ionica'] = 9
print(dict1)

#12
zile_saptamana = {'luni', 'marti', 'miercuri', 'joi', 'vineri'}
weekend = {'sambata', 'duminica'}
zile_saptamana.add('luni')
print(zile_saptamana)

#13
if weekend in zile_saptamana:
    print('weekend este un subset din zile saptamana')
else:
    print('weekend nu este un subset')

#14
zile_saptamana.intersection(weekend)
print(zile_saptamana)
weekend.intersection(zile_saptamana)
print(weekend)

#15
zile_saptamana.intersection_update(weekend)
print(zile_saptamana)
weekend.intersection_update(zile_saptamana)
print(weekend)
