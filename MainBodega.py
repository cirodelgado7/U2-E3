from ManejadorCamion import ManejadorCam
from ClaseCosecha import Cosecha
from MenuBodega import Menu

if __name__ == '__main__':
    mc = ManejadorCam()
    mc.testCamiones()
    c = Cosecha()
    c.testCosecha()
    c.agregarCosecha(mc)
    menu = Menu()
    salir = False
    while not salir:
        print("\n-----------------Menu--------------------")
        print(" 1 - Consultar cantidad de kilos descargados")
        print(" 2 - Listar descargas por día")
        print(" 3 - Salir")
        op = int(input(' Ingrese una opcion: '))
        menu.opcion(op,mc,c)
        if op == 3:
            salir = True

