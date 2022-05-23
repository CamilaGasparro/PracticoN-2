
class Conjunto:
    __elementos = []

    def __init__(self, elementos = []):
        self.__elementos = elementos

    def __str__(self):
        return str(self.__elementos)

    def __add__(self, conjunto):
        suma = self.__elementos + conjunto.getElementos()
        resultado = []
        for item in suma:
            if item not in resultado:
                resultado.append(item)
        
        return Conjunto(resultado)

    def __sub__(self, conjunto):
        resultado = []
        for item in self.__elementos:
            if item not in conjunto.getElementos():
                resultado.append(item)

        return Conjunto(resultado)

    def __eq__(self, conjunto):
        conjunto1 = self.__elementos
        conjunto2 = conjunto.getElementos()

        if len(conjunto1) != len(conjunto2):
            return False     

        conjunto1.sort()
        conjunto2.sort()
        i = 0

        while(i < len(conjunto1)):
            if conjunto1[i] != conjunto2[i]:
               return False
            i = i + 1
        
        return True

    def getElementos(self):
        return self.__elementos
