from Menu import Menu
from Conjunto import Conjunto


if __name__ == '__main__':
    menu = Menu()
    menu.getOpciones()
    A = Conjunto([1,2,3,4])
    B = Conjunto([3,6,9])
    opcion = int(input("Ingrese una opcion: "))
    menu.opcion(opcion, A, B)
