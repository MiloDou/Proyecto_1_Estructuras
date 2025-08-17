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
        print("\n      1) Registrar trabajadores.")
        print("      2) BUscar trabajadores por servicio")
        print("      3) Listar trabajadores")
        print("      4) Salir\n")

        