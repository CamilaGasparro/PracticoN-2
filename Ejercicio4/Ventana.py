class Ventana:
    __titulo = ''
    __coordXVertSupIzq = 0
    __coordYVertSupIzq = 0
    __coordXVertInfDer = 500
    __coordYVertInfDer = 500

    def __init__(self, titulo='', coordXVertSupIzq=0, coordYVertSupIzq=0, coordXVertInfDer=500, coordYVertInfDer=500):
        self.__titulo = titulo
        self.__coordXVertSupIzq = coordXVertSupIzq
        self.__coordYVertSupIzq = coordYVertSupIzq
        self.__coordXVertInfDer = coordXVertInfDer
        self.__coordYVertInfDer = coordYVertInfDer

    def mostrar(self):
        print('Titulo: {} \n{}{}-----\n |-----|\n |-----|\n |-----{}{}\n'.format(self.__titulo, self.__coordXVertSupIzq, self.__coordYVertSupIzq, self.__coordXVertInfDer, self.__coordYVertInfDer))

    def getTitulo (self):
        return self.__titulo

    def alto(self):
        return self.__coordYVertInfDer - self.__coordYVertSupIzq

    def ancho(self):
        return self.__coordXVertInfDer - self.__coordXVertSupIzq

    def moverDerecha(self, unidad ):
        self.__coordXVertInfDer += unidad
        self.__coordXVertSupIzq += unidad

    def moverIzquierda(self, unidad):
        self.__coordXVertInfDer -= unidad
        self.__coordXVertSupIzq -= unidad

    def bajar(self, unidad=0):
        self.__coordYVertInfDer -= unidad
        self.__coordYVertSupIzq -= unidad

    def subir(self, unidad=0):
        self.__coordYVertInfDer += unidad
        self.__coordYVertSupIzq += unidad
