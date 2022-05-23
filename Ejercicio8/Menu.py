import os


class Menu:
    __switcher= None

    def __init__(self):
        self.__switcher = {
            1: self.opcion1,
            2: self.opcion2,
            3: self.opcion3,
            4: self.salir
        }

    def getSwitcher(self):
        return self.__switcher

    def getOpciones(self):
        os.system("cls") #OS Operative system, system son las funciones del sistema operativo.
        print("1. Union de conjuntos\n2. Diferencia de conjuntos\n3. Igualdad de conjuntos\n4. Salir")

    def opcion(self, op, A, B):
        func = self.__switcher.get(op, lambda: print("Opcion invalida"))
        func(A, B)

    def salir(self):
        print('Salir')

    def opcion1(self, A, B):
        C = A + B
        print("La union de A + B es igual a: ", C)
    
    def opcion2(self, A, B):
        C = A - B
        print('La diferencia de A - B  es igual a: ', C)

    def opcion3(self, A, B):
        C = A == B
        if C:
            print('Son iguales')
        else:
            print('No son iguales')
