from Email import Email
import csv


def leerArchivo():
    nuevoArreglo = []
    with open('archivo.csv')as File:
        reader = csv.reader(File, delimiter=',')
        
        for row in reader:
            nuevoArreglo.append(row)
            
    return nuevoArreglo[0]

def creacionDeCuenta(correo):
    valid = False
    print(' - Crear cuenta')

    while not valid:
        valid = correo.crearCuenta(input('\t.Ingrese su email: '))

    nombre=input('\t.Ingrese el nombre: ')
    print('\n < Cuenta creada correctamente! > \n')
    print('Estimado {} te enviaremos tus mensajes a la direccion {}\n'.format(nombre, correo.retornaEmail()))

def cambiarClave(correo):
    valid = False
    print(' - Cambio de clave')
    
    while not valid:
        valid= correo.cambiarContraseña(correo)
        
    print('\n < Cambio de contraseña realizado > ')


def contarCorreos():
    contar= 0
    
    print(' Contar correos por dominio')
    listaDeMails = leerArchivo()
    dominioABuscar = input(" Ingrese dominio a buscar: ")
    
    print(listaDeMails)
    
    for email in listaDeMails:
        if(email.split('@')[1].split('.')[1] == dominioABuscar):
            contar += 1
    
    print(" La cantidad de correos con este dominio son: {}".format(contar))

class Main:
    
    unMail= Email()
    creacionDeCuenta(unMail)
    cambiarClave(unMail)
    contarCorreos()

