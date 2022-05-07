from Registro import Registro
import csv


class ManejadorVM:
    __filas = 30
    __columnas = 24
    __lista_vm = []

    def __init__(self, filas=30, columnas=24):
        self.__filas = filas
        self.__columnas = columnas
        self.__lista_vm = []

    def __str__(self):
        s = ''
        for i in range(self.__filas):
            for j in range(self.__columnas):
                print(self.__lista_vm[i][j])
        return s

    def testVM(self):
        for i in range(self.__filas):
            self.__lista_vm.append([0] * self.__columnas)
        archivo = open('Variables Meteorológicas.csv')
        reader = csv.reader(archivo, delimiter=',')
        bandera = True
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
                dia = int(fila[0])
                hora = int(fila[1])
                temperatura = int(fila[2])
                humedad = int(fila[3])
                presion = int(fila[4])
                self.__lista_vm[dia - 1][hora] = Registro(temperatura, humedad, presion)
        archivo.close()

    def mostrar(self):
        print(" Mostrar para cada variable el día y hora de menor y mayor valor")
        mayorT = self.__lista_vm[0][0].getTemperatura()
        menorT = self.__lista_vm[0][0].getTemperatura()
        mayorH = self.__lista_vm[0][0].getHumedad()
        menorH = self.__lista_vm[0][0].getHumedad()
        mayorP = self.__lista_vm[0][0].getPresion()
        menorP = self.__lista_vm[0][0].getPresion()
        DmayorT = 0
        HmayorT = 0
        DmenorT = 0
        HmenorT = 0
        DmayorH = 0
        HmayorH = 0
        DmenorH = 0
        HmenorH = 0
        DmayorP = 0
        HmayorP = 0
        DmenorP = 0
        HmenorP = 0
        for i in range(self.__filas):
            for j in range(self.__columnas):
                if self.__lista_vm[i][j].getTemperatura() >= mayorT:
                    mayorT = self.__lista_vm[i][j].getTemperatura()
                    DmayorT = self.__lista_vm[i][j].getDia()
                    HmayorT = self.__lista_vm[i][j].getHora()
                if self.__lista_vm[i][j].getTemperatura() <= menorT:
                    menorT = self.__lista_vm[i][j].getTemperatura()
                    DmenorT = self.__lista_vm[i][j].getDia()
                    HmenorT = self.__lista_vm[i][j].getHora()
                if self.__lista_vm[i][j].getHumedad() >= mayorH:
                    mayorH = self.__lista_vm[i][j].getHumedad()
                    DmayorH = self.__lista_vm[i][j].getDia()
                    HmayorH = self.__lista_vm[i][j].getHora()
                if self.__lista_vm[i][j].getHumedad() <= menorH:
                    menorH = self.__lista_vm[i][j].getHumedad()
                    DmenorH = self.__lista_vm[i][j].getDia()
                    HmenorH = self.__lista_vm[i][j].getHora()
                if self.__lista_vm[i][j].getPresion() >= mayorP:
                    mayorP = self.__lista_vm[i][j].getPresion()
                    DmayorP = self.__lista_vm[i][j].getDia()
                    HmayorP = self.__lista_vm[i][j].getHora()
                if self.__lista_vm[i][j].getPresion() <= menorP:
                    menorP = self.__lista_vm[i][j].getPresion()
                    DmenorP = self.__lista_vm[i][j].getDia()
                    HmenorP = self.__lista_vm[i][j].getHora()
        print('Mayor Temperatura')
        print('Dia = {}'.format(DmayorT))
        print('Hora = {}'.format(HmayorT))
        print('Menor Temperatura')
        print('Dia = {}'.format(DmenorT))
        print('Hora = {}'.format(HmenorT))
        print('Mayor Humedad')
        print('Dia = {}'.format(DmayorH))
        print('Hora = {}'.format(HmayorH))
        print('Menor Humedad')
        print('Dia = {}'.format(DmenorH))
        print('Hora = {}'.format(HmenorH))
        print('Mayor Presión')
        print('Dia = {}'.format(DmayorP))
        print('Hora = {}'.format(HmayorP))
        print('Menor Presión')
        print('Dia = {}'.format(DmenorP))
        print('Hora = {}'.format(HmenorP))

    def indicar(self):
        print(" Indicar la temperatura promedio mensual por cada hora")
        cero = 0
        una = 0
        dos = 0
        tres = 0
        cuatro = 0
        cinco = 0
        seis = 0
        siete = 0
        ocho = 0
        nueve = 0
        diez = 0
        once = 0
        doce = 0
        trece = 0
        catorce = 0
        quince = 0
        dieciseis = 0
        diecisiete = 0
        dieciocho = 0
        diecinueve = 0
        veinte = 0
        veintiuno = 0
        veintidos = 0
        veintitres = 0
        for i in range(self.__filas):
            cero += self.__lista_vm[i][0].getTemperatura()
            una += self.__lista_vm[i][1].getTemperatura()
            dos += self.__lista_vm[i][2].getTemperatura()
            tres += self.__lista_vm[i][3].getTemperatura()
            cuatro += self.__lista_vm[i][4].getTemperatura()
            cinco += self.__lista_vm[i][5].getTemperatura()
            seis += self.__lista_vm[i][6].getTemperatura()
            siete += self.__lista_vm[i][7].getTemperatura()
            ocho += self.__lista_vm[i][8].getTemperatura()
            nueve += self.__lista_vm[i][9].getTemperatura()
            diez += self.__lista_vm[i][10].getTemperatura()
            once += self.__lista_vm[i][11].getTemperatura()
            doce += self.__lista_vm[i][12].getTemperatura()
            trece += self.__lista_vm[i][13].getTemperatura()
            catorce += self.__lista_vm[i][14].getTemperatura()
            quince += self.__lista_vm[i][15].getTemperatura()
            dieciseis += self.__lista_vm[i][16].getTemperatura()
            diecisiete += self.__lista_vm[i][17].getTemperatura()
            dieciocho += self.__lista_vm[i][18].getTemperatura()
            diecinueve += self.__lista_vm[i][19].getTemperatura()
            veinte += self.__lista_vm[i][20].getTemperatura()
            veintiuno += self.__lista_vm[i][21].getTemperatura()
            veintidos += self.__lista_vm[i][22].getTemperatura()
            veintitres += self.__lista_vm[i][23].getTemperatura()
        print('00:00 = {:.2f}'.format(cero / 30))
        print('01:00 = {:.2f}'.format(una / 30))
        print('02:00 = {:.2f}'.format(dos / 30))
        print('03:00 = {:.2f}'.format(tres / 30))
        print('04:00 = {:.2f}'.format(cuatro / 30))
        print('05:00 = {:.2f}'.format(cinco / 30))
        print('06:00 = {:.2f}'.format(seis / 30))
        print('07:00 = {:.2f}'.format(siete / 30))
        print('08:00 = {:.2f}'.format(ocho / 30))
        print('09:00 = {:.2f}'.format(nueve / 30))
        print('10:00 = {:.2f}'.format(diez / 30))
        print('11:00 = {:.2f}'.format(once / 30))
        print('12:00 = {:.2f}'.format(doce / 30))
        print('13:00 = {:.2f}'.format(trece / 30))
        print('14:00 = {:.2f}'.format(catorce / 30))
        print('15:00 = {:.2f}'.format(quince / 30))
        print('16:00 = {:.2f}'.format(dieciseis / 30))
        print('17:00 = {:.2f}'.format(diecisiete / 30))
        print('18:00 = {:.2f}'.format(dieciocho / 30))
        print('19:00 = {:.2f}'.format(diecinueve / 30))
        print('20:00 = {:.2f}'.format(veinte / 30))
        print('21:00 = {:.2f}'.format(veintiuno / 30))
        print('22:00 = {:.2f}'.format(veintidos / 30))
        print('23:00 = {:.2f}'.format(veintitres / 30))

    def listar(self):
        print(" Dado un número de día listar los valores de las tres variables para cada hora del día dado")
        d = int(input('Ingrese el dia: '))
        print('%12s%15s%10s%12s'%('Hora', 'Temperatura', 'Humedad', 'Presión'))
        for i in range(self.__columnas):
            print(self.__lista_vm[d-1][i])
