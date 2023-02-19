from abc import abstractmethod, ABC
#ABSTRACTION
class FormaGeometrica:
    PI = 3.14

    def descriere(self):
        print("Cel mai probabil am colturi")

# INHERITANCE
class Patrat(FormaGeometrica):
    latura = None
    def __init__(self,latura):
        self.latura = latura

    __latura = 6

    def get_latura(self):
        return self.__latura

    def set_latura(self, latura_dorita):
        self.__latura = latura_dorita

    def latura(self):
        self.__latura = None

class Cerc(FormaGeometrica):
    raza = None

    def __init__(self,raza):
        self.raza = raza

    __raza = 7

    def get_raza(self):
        return self.__raza

    def set_raza(self, raza_dorita):
        self.__raza = raza_dorita

    def raza(self):
        self.__raza = None

    def descriere_cerc(self):
        print("Eu nu am colturi")

patrat1 = Patrat(6)
print(patrat1.latura)
print(patrat1.descriere())

cerc1 = Cerc(9)
print(cerc1.raza)
print(cerc1.descriere_cerc())

