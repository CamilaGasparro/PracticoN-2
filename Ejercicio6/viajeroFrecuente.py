#clase viajero
class viajeroFrecuente:
    __num_viajero = 0
    __DNI = " "
    __nombre = " "
    __apellido = " "
    __millasacumuladas = 0
    
    #constructor
    def __init__(self, numeroViajero, dni, nombre, apellido, millas):
        self.__num_viajero = numeroViajero
        self.__DNI = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millasacumuladas = millas
        
    #metodos instanciables
        
    def cantidadTotaldeMillas(self):
        return self.__millasacumuladas
    
    def acumularMillas(self, millasacumuladas):
        
        millas = int(millasacumuladas)
        
        if millasacumuladas > 0:
            self.__millasacumuladas = self.__millasacumuladas + millas
            print(" Resultado de millas: " + self.__millasacumuladas)
    
    def canjearMillas(self, millas):
        xmillas = int(millas)
        
        if self.__millasacumuladas > 0:
            self.__millasacumuladas = self.__millasacumuladas - xmillas
            print("Resultado de millas: " + self.__millasacumuladas)
            
    def getNumeroViajero(self):
        return self.__num_viajero

    def __gt__(self):
        pass

    def __sub__(self):
        pass

    def __add__(self):
        pass 