import os


class Excepts:
    def Clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def Continue():
        input("\n\033[90m  Presiona ENTER para continuar...\033[0m")
        Excepts.Clear()

    def Empty(prompt):
        while True:
            valor = input(prompt).strip()
            if valor == "":
                
                print("\033[31m ❌ Este campo no puede estar vacío. Intenta de nuevo.\033[0m")
            else:
                return valor

    def Wrong_type():
        print("\033[31m ❌ Tipo de dato inválido. Intenta de nuevo.\033[0m")
    
    def StartContinue():
        input("\033[90m           Presiona ENTER para iniciar...\033[0m")
        Excepts.Clear()

    def Default():
        input("\033[90m   ❌ Esta opción no existe, intenta de nuevo.\033[0m")
        print(" "+Excepts.Continue())
