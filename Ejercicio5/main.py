import csv
import os
from PlanAhorro import PlanAhorro


def buscaPlan(codigo, planes):
    i=0
    while (codigo != planes[i].getCodigoPlan() and i < len(planes) ):
        i+=1
    if i < len(planes):
        return planes[i]
    else:
        return None
    
    input('\n\n<< press any key to continue >>')


def option1(planes):
    for element in planes:
        print(element)

    codigo = input('Ingrese el codigo del vehiculo: ')
    planResult = buscaPlan(codigo, planes)

    if planResult != None:
        nuevoValor = input('Ingres el nuevo valor del vehiculo: ')
        planResult.setValorVehiculo(nuevoValor)
        print(planResult)
    else:
        print('Valor ingresado invalido')
    
    input('\n\n<< press any key to continue >>')


def option2(planes):
    valor = int(input("Ingresar un valor de cuota: "))

    for element in planes:
        if( valor <= element.getValorCuota()):
            print(element)
    
    input('\n\n<< press any key to continue >>')


def option3(planes):
    for element in planes:
        print(element)

    codigo = input('Ingrese el codigo del vehiculo: ')
    planResult = buscaPlan(codigo, planes)

    print("Monto que debe pagar para licitar el vehiculo: ", planResult.getMontoParaLicitar()) 
    input('\n\n<< press any key to continue >>')

def option4(planes):
    for element in planes:
        print(element)

    codigo = input('Ingrese el codigo del vehiculo: ')
    planResult = buscaPlan(codigo, planes)
    
    cuotas = input("Ingresar cantidad de cuotas para licitar: ")
    planResult.setCuotasParaLicitar(cuotas)
    input('\n\n<< press any key to continue >>')

select = {1: option1, 2: option2, 3: option3, 4: option4}

def menu(opc, planes):
    func = select.get(opc, lambda: print("Opcion Incorrecta"))
    func(planes)

def leerArchivo():
    planes = []
    with open('planes.csv') as File:
        reader = csv.reader(File, delimiter = ';')
        for row in reader:
            object = PlanAhorro(row[0], row[1], row[2], int(row[3]))
            planes.append(object);

    return planes;

if __name__ == '__main__':
    planes = leerArchivo()
    flag = False

    while not flag:
        os.system("cls")
        print('\tMenu - Cantidad total de planes ({})'.format(len(planes)))
        print('1:Actualizar el valor del vehiculo')
        print('2:Vehiculos dado un valor de cuota')
        print('3:Monto que se debe pagar para licitar el vehiculo: ')
        print('4:Modificar cantidad de cuotas para licitar el vehiculo')
        print('5:Salir')
        opc = int(input('\nIngrese Opcion: '))
        if opc != 5 : menu(opc, planes)
        flag = int(opc) == 5
