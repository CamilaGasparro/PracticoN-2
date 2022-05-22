import os
from ManejadorViajero import ManejadorViajero

class Menu:
    __switcher= None

    def __init__(self):
        self.__switcher = {
            1: self.opcion1,
            2: self.opcion2,
            3: self.opcion3,
            4: self.opcion4,
            5: self.opcion5,
            6: self.opcion6,
            7: self.opcion7,
            8: self.salir
        }

    def getSwitcher(self):
        return self.__switcher

    def getOpciones(self):
        os.system("cls") #OS Operative system, system son las funciones del sistema operativo.
        print("1. Consultar cantidad de millas\n2. Acumular millas\n3. Canjear millas\n4. Viajero con mas millas\n5. Sumar millas\n6. Canjear millas\n7.Comparar cantidad de millas acumuladas de un viajero\n8. Salir")

    def opcion(self, op, listViajeros):
        func = self.__switcher.get(op, lambda: print("Opcion invalida"))
        func(listViajeros)

    def salir(self):
        print('Salir')

    def opcion1(self, listViajeros):
        band = False

        num = int(input('Ingrese el numero de viajero: ')) - 1

        viajero = listViajeros.findViajero(num)

        if viajero:
            print("Las millas acumuladas son : ", viajero.getMillasAcumuladas())

        else:
            print('Numero de viajero incorrecto')


    def opcion2(self, listViajeros):
        band = False

        num = int(input('Ingrese el numero de viajero: ')) - 1

        viajero = listViajeros.findViajero(num)

        if viajero:
            cant = int(input('Ingrese cantidad de millas acumuladas: '))
            viajero.setMillasAcumuladas(cant)


    def opcion3(self, listViajeros):
        band = False

        num = int(input('Ingrese el numero de viajero: ')) - 1

        viajero = listViajeros.findViajero(num)

        if viajero:
            millasACanjear = int(input('Ingrese la cantidad de millas a canjear: '))
            viajero.canjearMillas(millasACanjear)

    def opcion4(self, listViajeros):
        lista = listViajeros.getViajeroList()
        maxViajero = lista[0]

        for viajero in lista:
            if viajero > maxViajero:
                maxViajero = viajero
        
        print("El viajero con mayor cantidad de millas acumuladas es: ", maxViajero)


    def opcion5(self, listViajeros):
 
        num = int(input('Ingrese el numero de viajero: ')) - 1

        viajero = listViajeros.findViajero(num)

        if viajero:
            cant = int(input("Ingrese millas a acumular: "))
            viajero = cant + viajero
            print(viajero)

        else:
            print('Numero de viajero incorrecto')
            
    def opcion6(self, listViajeros):

        num = int(input('Ingrese el numero de viajero: ')) - 1
        
        viajero = listViajeros.findViajero(num)

        if viajero:
            cant = int(input("Ingrese cantidad de millas a canjear: "))
            viajero = viajero - cant
            print(viajero)
        else:
            print('Numero de viajero incorrecto')


    def opcion7(self, listViajeros):
        num = int(input('Ingrese el numero de viajero: ')) - 1

        viajero = listViajeros.findViajero(num)

        if viajero:
            cant= int(input("Ingrese cantidad de millas a comparar: "))
            result = cant == viajero 
            if result:
                print("la cantidad de millas son iguales ")
            else:
                print("la cantidad de millas son distintas")
        else:
            print('Numero de viajero incorrecto')







