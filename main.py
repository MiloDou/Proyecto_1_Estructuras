from menus import Menus
from excepts import Excepts
from providers import Provider

def main():

    Menus.Start()  

    while True:
        Menus.Menu()
        try:
            option = int(input('    Elige una opcion: '))
        except ValueError:
            print("\033[31m    Debes ingresar un número.\033[0m")
            Excepts.Continue()
            continue

        match option:
            case 1:
                Menus.Op1()
                
            case 2:
               Menus.Op2()

            case 3:
                Menus.Op3()

            case 4:
                Menus.Op4()

            case 5:
                Menus.Salir()
                break

            case _:
                Excepts.Default()

                
if __name__ == "__main__":
    main()
