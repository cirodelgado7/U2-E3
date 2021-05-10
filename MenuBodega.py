import sys

class Menu:

    __switcher = None

    def __init__(self):
        __switcher = None
        self.__switcher = {
            1: self.consultarKilosDescargados,
            2: self.listarPorDia,
            3: self.salir
            }

    def getSwitcher(self):
        return self.__switcher

    def opcion(self,op,mc,c):
        func = self.__switcher.get(op,lambda: print("Opción no válida"))
        func(mc,c)

    def consultarKilosDescargados(self,mc,c):
        print(c)
        print("\n 1 - Consultar cantidad de kilos descargados")
        i = int(input('Ingrese el identificador de Camión: '))
        t = c.consultarTotal(i)
        print('\n El total de kilos descargados es:',t)

    def listarPorDia(self,mc,c):
        print("\n 2 - Listar descargas por día")
        d = int(input("\n Ingrese el Dia: "))
        mc.listar(c,d)

    def salir(self,mc,c):
        sys.exit(0)