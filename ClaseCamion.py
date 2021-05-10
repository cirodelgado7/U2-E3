class Camion:

    __identificador = 0
    __nombre = ''
    __patente = ''
    __marca = ''
    __tara = ''

    def __init__(self,identificador, nombre, patente, marca, tara):
        self.__identificador = identificador
        self.__nombre = nombre
        self.__patente = patente
        self.__marca = marca
        self.__tara = tara

    def __str__(self):
        return " %3d   %13s    %15s    %20s    %25s" % (self.__identificador, self.__nombre, self.__patente, self.__marca, self.__tara)

    def obtenerIdentificador(self):
        return self.__identificador

    def obtenerNombre(self):
        return self.__nombre

    def obtenerPatente(self):
        return self.__patente

    def obtenerMarca(self):
        return self.__marca

    def obtenerTara(self):
        return self.__tara