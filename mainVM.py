from ManejadorVM import ManejadorVM
from menuVM import Menu

if __name__ == '__main__':
    vm = ManejadorVM()
    vm.testVM()
    menu = Menu()
    menu.opciones(vm)
