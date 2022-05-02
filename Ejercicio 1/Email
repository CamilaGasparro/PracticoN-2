import re

PATTERN_EMAIL = "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
PATTERN_PASS = re.compile("^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$")

#clase email
class Email:
    __idCuenta = " "
    __dominio = " "
    __tipoDominio = " "
    __contraseña = " "
    
    #constructor 
    def __init__(self, idCuenta="", dominio="", tipo="", clave=""):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDominio = tipo
        self.__contraseña = clave
        
    #metodos instanciables
    
    def retornaEmail(self):
        return self.__idCuenta + "@" + self.__dominio + "." + self.__tipoDominio
    
    def getDominio(self):
        return self.__dominio
    
    def crearCuenta(self, email):
        
        if(re.search(PATTERN_EMAIL,email)):
            mitadEmail= email.split('@',1)
            self.__tipoDominio = mitadEmail[1].split('.')[0]
            self.__idCuenta = mitadEmail[0]
            self.__dominio = mitadEmail[1]
            
            match= input("Ingrese la contraseña: ")
            
            if(re.search(PATTERN_PASS, match)):
               self.__contraseña= match
               return True;
            else:
                print("contraseña invalida, intenta de nuevo \n")
                return False;
        else:
            print("Correo electronico invalido \n")
            return False;
        
    def cambiarContraseña(self, email):
        
        match= input("Ingresar clave actual: ")
        
        if(re.search(PATTERN_PASS, match) and match == self.__contraseña):
            
            newMatch= input(" Ingresar nueva clave: ")
            
            
            if(re.search(PATTERN_PASS, newMatch)):
                self.__contraseña= newMatch
                return True
            else: 
                print(" Clave no valida, intente de nuevo")
                return False
        else:
            print(" Clave incorrecta, intente de nuevo")
            return False
