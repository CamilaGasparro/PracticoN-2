import os
from ManejadorViajero import ManejadorViajero

class Menu:
    __switcher = None
    
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
        print("1.Consultar cantidad de millas\n2.Acumular millas\n3.Canjear millas\n4.Salir")
        os.system("cls")
        
    def salir(self):
        print("Salir")
        
    def opcion(self, op, listViajeros):
        func = self.__switcher.get(op, lambda: print("Opcion invalida"))
        func(listViajeros)
        
    def opcion1(self, listViajeros):
        band = False
        
        num= int(input("Ingrese el numero de viajero: "))
        
        viajero = listViajeros.findViajero(num)
        
        if viajero:
            print("Las millas acumuladas son: ", viajero.cantidadTotalDeMillas())
        else:
            print("Numero de viajero incorrecto o no encontrado")
        
        viajero.cantidadTotalDeMillas() > viajero.cantidadTotalDeMillas()
        
    def opcion2(self, listViajeros):
        band = False
        
        num = int(input("Ingrese el numero de viajero: "))
        
        viajero = listViajeros.findViajero(num)
        
        if viajero:
            cant= int(input("Ingrese cantidad de millas acumuladas: "))
            viajero.acumularMillas(cant)
            
    def opcion3(self, listViajeros):
        band = False
        
        num = int(input("Ingrese el numerode viajero: "))
            
        viajero = listViajeros.findViajero(num)
        
        if viajero:
            millasACanjear = int( input("Ingrese cantidad de millas a canjear: "))
            viajero.canjearMillas(millasACanjear)