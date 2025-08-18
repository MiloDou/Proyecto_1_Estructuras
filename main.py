from menus import Menus
from excepts import Excepts
from b_tree import BTree
from providers import Provider
from random import randint

def main():

    Menus.Start()
    tree = BTree(3)  

    while True:
        Menus.Menu()
        try:
            option = int(input('    Elige una opcion: '))
        except ValueError:
            print("\033[31m   Debes ingresar un número.\033[0m")
            Excepts.Continue()
            continue

        match option:
            case 1:
                print("----Registrar trabajadores")

                new_id = Excepts.UniqueID(randint)
                new_name = Excepts.Empty("Ingrese el nombre del trabajador: ")
                new_service = Excepts.Empty("Ingrese el servicio del trabajador: ")
                new_rating = Excepts.InputInt("Ingrese la calificación del trabajador (1-5): ", 1, 5)
                
                new_provider = Provider(new_id, new_name, new_service, new_rating)
                tree.insert(new_provider)
                print(f"Trabajador: {new_name}| ID: {new_id}\n ¡Registrado exitosamente!.")
                tree.display()
                Excepts.Continue()
                
            case 2:
               if len(tree) == 0:
                   print("\033[31m   No existen trabajadores registrados.\033[0m")
               else:
                   print("Buscar trabajadores por servicio")
                   service = input('Ingrese el servicio: ')
                   searching = tree.search(service)
                   if searching:
                       print(f"Se encontraron {len(searching)} trabajadores {service}s:\n")
                       for s in searching:
                           print(s)

                   else:
                       print(f"\033[31m   No se encontraron trabajadores con servicio '{service}'.\033[0m")
                
               Excepts.Continue()

            case 3:
                if len(tree) == 0:
                    print("\033[31m   No existen trabajadores registrados.\033[0m")
                else:
                    print("Listar trabajadores")
                    all_providers = tree.get_all_providers()
                    print("\n--- Ranking de calificación ---")
                    Provider.ranking(all_providers)
                    print("\n--- Orden alfabético ---")
                    Provider.alphabetic_orden(all_providers)
                
                Excepts.Continue()

            case 4:
                print("Salir del programa")
                break

            case _:
                Excepts.Default()

                
if __name__ == "__main__":
    main()
