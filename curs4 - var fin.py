#1
'''masini = ['Audi', 'Volvo', 'BMW','Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#1.1 cu for
for i in range(0,len(masini),1):
    print(f'Masina mea preferata este {masini[i]}')


#1.2 cu for each
for masina in masini:
    print(f'Masina mea preferata este', {masina})

# 1.3 cu while
masina = 0
while masina < len(masini):
    print("Masina mea preferata este " + masini[masina])
    masina = masina + 1'''

#2.
'''masini = ['Audi', 'Volvo', 'BMW','Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_upper =[]
for i in range(1,len(masini)-1,1):
    print(masini[i].upper())'''

#3
'''masini = ['Audi', 'Volvo', 'BMW','Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Mercedes':
        break
    print('Am gasit masina dorita de dvs.')
else:
    print('Am gasit masina X. Mai cautam')
#4
masini = ['Audi', 'Volvo', 'BMW','Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Lastun' or masina == 'Trabant':
        continue
    print('S-ar putea sa va placa', {masina})'''
#5
masini_vechi=[]
masini = ['Audi', 'Volvo', 'BMW','Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == "Lastun" :
        masini_vechi.append(masina)
    if masina == "Trabant":
        masini_vechi.append(masina)
    print(masini_vechi)
masini[5] = "Tesla"
masini[7] = "Tesla"
print(masini)

'''#6
pret_masini = {
    'Dacia':6800,
    'Lastun':500,
    'Opel': 1100,
    'Audi':19000,
    'BMW':23000
}
for x,y in pret_masini.items():
    if y < 15000:
        print(f'Pentru un buget de sub 15 000 euro puteti alege masina' + x)


#7
numere = [5,7,3,9,3,3,1,0,-4,3]
contor = 0
for numar in numere:
    if numar ==3:
        contor = contor+1
print(contor)

#8
numere = [5,7,3,9,3,3,1,0,-4,3]
sum = 0
for i in numere:
    sum += i
print(sum)

#9
numere = [5,7,3,9,3,3,1,0,-4,3]
max = 0
for i in range(0, len(numere)):
    if numere[0] > numere[1]:
        max = numere[0]
    else:
        max = numere[1]
    if numere[1] > numere[2]:
        max = numere[1]
    else:
        max=numere[2]
print(max)'''

#10
numere = [5,7,3,9,3,3,1,0,-4,3]
numere_invers = []
for numar in numere:
    if numar > 0:
        numar = - numar
    else:
        numar = numar*-1
    numere_invers.append(numar)
print(numere_invers)







#10
'''numere = [5,7,3,9,3,3,1,0,-4,3]
for i in numere:
    if i > 0:
        i = -i
    print(numere)'''

