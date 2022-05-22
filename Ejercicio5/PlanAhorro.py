class PlanAhorro:
    __codPlan = 0
    __modeloVehiculo = " "
    __versionVehiculo = " "
    __valorVehiculo = 0
    __canCuotasPlan = 60
    __cantCuotasPagas = 10


    def __init__(self, codPlan="", modeloVehiculo="", versionVehiculo="", valorVehiculo=0):
        self.__codPlan = codPlan
        self.__modeloVehiculo = modeloVehiculo
        self.__versionVehiculo = versionVehiculo
        self.__valorVehiculo = valorVehiculo

    def __str__(self):
        return 'El codigo del plan es: {}, modelo: {}, version: {} '.format(self.__codPlan, self.__modeloVehiculo, self.__versionVehiculo)

    def getValor(self):
        return self.__valorVehiculo

    def setValorVehiculo(self, valor):
        self.__valorVehiculo = valor 

    def getCodigoPlan(self):
        return self.__codPlan

    def getValorCuota(self):
        return (self.__valorVehiculo / self.__canCuotasPlan ) + self.__valorVehiculo * 0.10

    def getMontoParaLicitar(self):
        return self.__cantCuotasPagas * self.getValorCuota() 

    def setCuotasParaLicitar(self, cuotas):
        self.__cantCuotasPagas = cuotas