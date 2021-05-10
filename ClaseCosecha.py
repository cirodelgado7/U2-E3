import csv

class Cosecha:

    __listaCosecha = []

    def __init__(self):
        self.__listaCosecha = []

    def __str__(self):
        s = ""
        for lista in self.__listaCosecha:
            s += str(lista) + '\n'
        return s

    def testCosecha(self):
        archivo = open('Cosechas.csv')
        reader = csv.reader(archivo,delimiter=';')
        for fila in reader:
            self.__listaCosecha.append(fila)
        archivo.close()

    def mostrar(self):
        for fila in self.__listaCosecha:
            print(fila)

    def totalkilos (self,i):
        acu=0
        lon=len(self.__listaCosecha[i])
        for j in range(lon):
            acu=acu+self.__listaCosecha[i][j]
            print(acu)

    def agregarCosecha(self,mc):
        print('\n     ***** Bodega *****       ')
        print('***** Descarga de Cosechas *****')
        bandera = True
        while bandera:
            print('¿Desea registrar una descarga?')
            o = input('s/n: ')
            if o == 's':
                d = int(input('Día: '))
                i = int(input('Identificador de Camión: '))
                indice = mc.buscarCamion(i)
                unCamion = mc.obtenerCamion(indice)
                tara = float(unCamion.obtenerTara())
                k = float(input('Cantidad de Kilos: '))
                self.__listaCosecha[indice][d-1] = k - tara + float(self.__listaCosecha[indice][d-1])
            else:
                bandera = False

    def consultarKilos(self,i,d):
        return self.__listaCosecha[i][d-1]

    def consultarTotal(self,iden):
        a = 0.0
        for i in range(len(self.__listaCosecha)):
            a += float(self.__listaCosecha[iden-1][i])
        return a