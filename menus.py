import os
import time
import sys
from excepts import Excepts


class Menus:
    def animate(text, delay=0.1):
        for letter in text:
            print(letter, end="", flush=True)
            time.sleep(delay)
    print()

    def Start():
        Excepts.Clear()
        linea = "\n\n\n\033[1;93m   ╔═════════════════════════════════════════════╗\033[0m"
        linea_inferior = "\033[1;93m   ╚═════════════════════════════════════════════╝\033[0m"

        print("\n" + linea)
        print("\033[1;93m   ║\033[0m", end="")
        Menus.animate("\033[1;97m            P R O Y E C T O  #1\033[0m", delay=0.05)
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
        print("\033[93m      4)\033[0m Salir\n")
    
    def Op1():
        Excepts.Clear()
        print("\n\033[1;93m   ╔═════════════════════════════════════════════╗\033[0m")
        print("\033[1;93m   ║\033[1;97m         REGISTRAR TRABAJADOR            \033[1;93m║")
        print("   ╚═════════════════════════════════════════════╝\033[0m")

        