#1
class Cerc:
    raza = None
    culoare = None
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descriere_cerc(self):
        print(f'Culoarea cercului este {self.culoare}')
        print(f' Raza cercului este {self.raza}')

    def pi_value(self):
        return 3.14

    def aria(self):
        return self.raza * self.raza* self.pi_value()

    def diametru(self):
        return self.raza + self.raza

    def circumferinta(self):
        return self.raza*2* self.pi_value()

cerc = Cerc(5,'roz')
cerc.descriere_cerc()
print(cerc.circumferinta())
print(cerc.aria())
print(cerc.diametru())


class Dreptunghi:
    lungime = None
    latime = None
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def aria(self):
        return self.lungime*self.latime

    def descriere(self):
        return print(f' Dreptunghiul are latimea de {self.latime} cm si lungimea de {self.lungime} cm si culoarea {self.culoare}')

    def perimetru(self):
        return (self.lungime *2) + (self.latime*2)


dreptunghi = Dreptunghi(5,8,'gri')

dreptunghi.descriere()
print(dreptunghi.aria())
print(dreptunghi.perimetru())
dreptunghi.culoare = 'roz'
print(dreptunghi.descriere())

#3
class Angajat:
    nume = None
    prenume = None
    salariu = None

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere(self):
        return print(f' Numele salariatului este {self.prenume} {self.nume} cu salariul {self.salariu}  lei.')

    def nume_complet(self):
        return print(f'Numele complet al angajatului este: {self.prenume} {self.nume}')

    def salariu_lunar(self):
        return print(f' Salariul lunar al angajatului este {self.salariu}')

    def salariu_anual(self):
        return self.salariu*12

    def marire_salariu(self):
        return self.salariu*1.10

angajat1 = Angajat('Ion', 'Ionescu', 5000)
angajat1.descriere()
angajat1.nume_complet()

print(angajat1.salariu_anual())
print(angajat1.marire_salariu())

#4
class Cont:
    iban = None
    titular_cont = None
    sold = None

    def __init__(self, iban,titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        return print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei')

    def debitare_cont(self,suma_debitata):
        return self.sold - suma_debitata


    def creditare_cont(self, suma_creditata):
        return self.sold + suma_creditata

cont1= Cont('RO01', 'Ion Ionescu', 2000)
print(cont1.afisare_sold())
print(cont1.creditare_cont(200))
print(cont1.debitare_cont(100))






