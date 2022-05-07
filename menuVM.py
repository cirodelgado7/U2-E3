import sys


class Menu:
    __switcher = None

    def __init__(self):
        __switcher = None
        self.__switcher = {
            1: self.mostrar,
            2: self.indicar,
            3: self.listar,
            4: self.salir
        }

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, vm):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func(vm)

    def opciones(self, vm):
        salir = False
        while not salir:
            print("\n-----------------Menu--------------------")
            print(" 1 - Mostrar")
            print(" 2 - Indicar")
            print(" 3 - Listar ")
            print(" 4 - Salir")
            op = int(input(' Ingrese una opcion: '))
            self.opcion(op, vm)
            if op == 4:
                salir = True

    def mostrar(self, vm):
        vm.mostrar()

    def indicar(self, vm):
        vm.indicar()

    def listar(self, vm):
        vm.listar()

    def salir(self, vm):
        sys.exit(0)
