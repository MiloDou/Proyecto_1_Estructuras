import os
import sys
from excepts import Excepts
from b_tree import BTree
from random import randint
from providers import Provider


class Menus:
    tree = BTree(3)

    def Start():
        Excepts.Clear()
        linea = "\n\n\n\033[1;93m   ╔═════════════════════════════════════════════╗\033[0m"
        linea_inferior = "\033[1;93m   ╚═════════════════════════════════════════════╝\033[0m"

        print("\n" + linea)
        print("\033[1;93m   ║\033[0m", end="")
        Excepts.animate("\033[1;97m            P R O Y E C T O  #1\033[0m", delay=0.05)
        print("\033[1;93m              ║\033[0m")
        print(linea_inferior + "\n")
        print("                Realizado por:")
        print("       Emilio Méndez y Fernanda Navarro\n")
        Excepts.StartContinue()


    def Menu():
        Excepts.Clear()
        print("\n\033[1;93m   ╔═════════════════════════════════════════════╗\033[0m")
        print("\033[1;93m   ║\033[1;97m            B I E N V E N I D O              \033[1;93m║")
        print("   ╚═════════════════════════════════════════════╝\033[0m")
        print("\n\033[93m      1)\033[0m Registrar trabajadores.")
        print("\033[93m      2)\033[0m BUscar trabajadores por servicio")
        print("\033[93m      3)\033[0m Listar trabajadores")
        print("\033[93m      4)\033[0m Exportar")
        print("\033[93m      5)\033[0m Salir\n")

    
    def Op1():
        Excepts.Clear()
        print("\n\033[1;93m   ╔═════════════════════════════════════════════╗\033[0m")
        print("\033[1;93m   ║\033[1;97m            REGISTRAR TRABAJADOR             \033[1;93m║")
        print("   ╚═════════════════════════════════════════════╝\033[0m\n")
        new_id = Excepts.UniqueID(randint)
        new_name = Excepts.Normalize(Excepts.Empty("    Nombre: "))
        new_service = Excepts.Normalize(Excepts.Empty("    Tipo de Servicio: "))
        new_rating = Excepts.InputInt("    Calificación del trabajador (1-5): ", 1, 5)

        new_provider = Provider(new_id, new_name, new_service, new_rating)
        Menus.tree.insert(new_provider)

        print(f"\n    Trabajador: {new_name}\n    ID: {new_id}\n\n\033[1;92m    ¡Registrado exitosamente!.")

        Menus.tree.display()
        print("\n")
        Excepts.Continue()
    
    def Op2():
        if len(Menus.tree) == 0:
            print("\033[31m   No existen trabajadores registrados.\033[0m")
        else:
            Excepts.Clear()
            print("\n\033[1;93m   ╔═════════════════════════════════════════════╗\033[0m")
            print("\033[1;93m   ║\033[1;97m            BUSCAR POR SERVICIO              \033[1;93m║")
            print("   ╚═════════════════════════════════════════════╝\033[0m\n")
            service = input('    Ingrese el servicio: ')
            searching = Menus.tree.search(service)
            if searching:
                print(f"    Se encontraron {len(searching)} trabajadores \"{service}\":\n")
                for s in searching:
                    print(s)
            else:
                print(f"\033[31m    No se encontraron trabajadores con servicio '{service}'.\033[0m")
        
        Excepts.Continue()
    
    def Op3():
        if len(Menus.tree) == 0:
            print("\033[31m    No existen trabajadores registrados.\033[0m")
        else:
            Excepts.Clear()
            print("\n\033[1;93m   ╔═════════════════════════════════════════════╗\033[0m")
            print("\033[1;93m   ║\033[1;97m            LISTAR TRABAJADORES              \033[1;93m║")
            print("   ╚═════════════════════════════════════════════╝\033[0m\n")
            all_providers = Menus.tree.get_all_providers()
            print("\033[1;97m    ══════════ Ranking de calificación ══════════\n\033[0m")
            Provider.ranking(all_providers)
            print("\n\033[1;97m    ═════════════ Orden alfabético ══════════════\n\033[0m")
            Provider.alphabetic_orden(all_providers)
                
        Excepts.Continue()
    
    def Op4():
        if len(Menus.tree) == 0:
            print("\033[31m    No existen trabajadores registrados.\033[0m")
        else:
            Excepts.Clear()
            print("\n\033[1;93m   ╔═════════════════════════════════════════════╗\033[0m")
            print("\033[1;93m   ║\033[1;97m              EXPORTAR ARCHIVO               \033[1;93m║")
            print("   ╚═════════════════════════════════════════════╝\033[0m\n")
            ##agregar lo de los archivos
                
        Excepts.Continue()

    def Salir():
        Excepts.animate("\033[1;97m    Saliendo...\033[0m", delay=0.1)
        Excepts.Clear()
        print("\n\033[1;93m   ╔═════════════════════════════════════════════╗\033[0m")
        print("\033[1;93m   ║\033[1;97m                A D I Ó S 😺                 \033[1;93m║")
        print("   ╚═════════════════════════════════════════════╝\033[0m\n")
