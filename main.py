from menus import Menus
from excepts import Excepts
from b_tree import BTree
from providers import Provider
from random import randint
def main():
    #Menus.Start()
    Menus.Menu()
    tree = BTree(3)  
    while True:
        option = int(input('Elige una opcion: '))
        match option:
            case 1:
                print("Registrar trabajadores")

                new_id = randint(1, 1000)  
                new_name = input("Ingrese el nombre del trabajador: ")
                new_service = input("Ingrese el servicio del trabajador: ")
                new_rating = int(input("Ingrese la calificación del trabajador (1-5): "))
                new_provider = Provider(new_id, new_name, new_service, new_rating)
                tree.insert(new_provider)
                print(f"Trabajador: {new_name}| ID: {new_id}\n ¡Registrado exitosamente!.")
                tree.display()

                
            case 2:
                print("Buscar trabajadores por servicio")
                search_id = input('Ingrese el ID: ')
                searching = tree.search(search_id)
                print(f'Se encontró el trabajador: {searching}')
            case 3:
                print("Listar trabajadores")
                ranking = Provider.ranking(tree)
                alphabetic = Provider.alphabetic_orden(tree)
                print(f'Los mejores ranqueados: {ranking}')
                print(f'Orden alfábetico de los empleados: {alphabetic}')
            case 4:
                print("Salir del programa")
                Excepts.Clear()
                False
            case _:
                Excepts.Default()
if __name__ == "__main__":
    main()
