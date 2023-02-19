#1
# o variabila este ca un sertar in care punem obiecte si le numim
#2
elev = "Matei"
pret = 12
gramaj = 15.6
este_acceptat = True

#3
print(type(elev))
print(type(pret))
print(type(gramaj))
print(type(este_acceptat))

#4
gramaj = round(gramaj)
print(type(gramaj))

#5
print(f'Elevul {elev} a platit {pret} lei pentru {gramaj}g de nuci.{este_acceptat}')

#6
nume_Prenume = input("Introduceti numele si prenumele")
print(f'Numele complet are {len(nume_Prenume)}')

#7
lungimea = int(input("introduceti lungimea dreptunghiului"))
latimea = int(input('Introduceti latimea dreptunghiului'))
print(lungimea*latimea)

#8
prop = "Coral is either the stupidest animal or the smartest rock"
print(prop.count('the'))

#9
prop = "Coral is eiTHEr THE stupidest animal or THE smartest rock"
print(prop.count('THE'))

# 10
prop = "Coral is either the stupidest animal ot the smartest rock"
prop.isnumeric()
print(prop.isnumeric())
