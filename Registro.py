class Registro:
    __temperatura = 0
    __humedad = 0
    __presion = 0

    def __init__(self, temperatura=0, humedad=0, presion=0):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion = presion

    def __str__(self):
        return " %10s  %10s  %10s  %10s" % (self.__temperatura, self.__humedad, self.__presion)

    def getTemperatura(self):
        return self.__temperatura

    def getHumedad(self):
        return self.__humedad

    def getPresion(self):
        return self.__presion

    def setTemperatura(self, t):
        self.__temperatura = t

    def setHumedad(self, h):
        self.__humedad = h

    def setPresion(self, p):
        self.__presion = p
