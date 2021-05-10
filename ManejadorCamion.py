import csv
from ClaseCamion import Camion
from ClaseCosecha import Cosecha

class ManejadorCam:

    __listaCamiones = []

    def __init__(self):
        self.__listaCamiones = []

    def __str__(self):
        s = ""
        for lista in self.__listaCamiones:
            s += str(lista) + '\n'
        return s

    def testCamiones(self):
        archivo = open('Camiones.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
              identificador = int(fila[0])
              nombre = fila[1]
              patente = fila[2]
              marca = fila[3]
              tara = int(fila[4])
              unCamion = Camion(identificador,nombre,patente,marca,tara)
              self.agregarCamion(unCamion)
        archivo.close()

    def agregarCamion(self,unCamion):
        self.__listaCamiones.append(unCamion)

    def buscarCamion(self, clave):
        for indice, Camion in enumerate(self.__listaCamiones):
            if Camion.obtenerIdentificador() == clave:
                return indice

    def obtenerCamion(self, indice):
        return self.__listaCamiones[indice]

    def listar(self,c,d):
        print('PATENTE\t    CONDUCTOR\t   CANTIDAD DE KILOS')
        for i in range(20):
            print('{:>6}{:>15}{:>15}'.format(self.__listaCamiones[i].obtenerPatente(),self.__listaCamiones[i].obtenerNombre(),c.consultarKilos(i,d)))