import os
import unicodedata
import time

class Excepts:
    generated_ids = set()

    def animate(text, delay=0.1):
        for letter in text:
            print(letter, end="", flush=True)
            time.sleep(delay)
    print()

    def Clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def Continue():
        input("\033[90m    Presiona ENTER para continuar...\033[0m")
        Excepts.Clear()

    def Empty(prompt):
        while True:
            valor = input(prompt).strip()
            if valor == "":
                
                print("\033[31m    Este campo no puede estar vacío. Intenta de nuevo.\n\033[0m")
            else:
                return valor
            
    def UniqueID(randint_func):
        while True:
            new_id = randint_func(1, 1000)
            if new_id not in Excepts.generated_ids:
                Excepts.generated_ids.add(new_id)
                return new_id
            
    def InputInt(prompt, min_val=None, max_val=None):
        while True:
            try:
                valor = int(input(prompt))
                if min_val is not None and valor < min_val:
                    print(f"\033[31m   Debe ser mayor o igual a {min_val}.\n\033[0m")
                elif max_val is not None and valor > max_val:
                    print(f"\033[31m    Debe ser menor o igual a {max_val}.\n\033[0m")
                else:
                    return valor
            except ValueError:
                print("\033[31m    Tipo de dato inválido. Intenta de nuevo.\n\033[0m")


    def StartContinue():
        input("\033[90m           Presiona ENTER para iniciar...\033[0m")
        Excepts.Clear()

    def Default():
        print("\033[31m    Esta opción no existe, intenta de nuevo.\033[0m")
        Excepts.Continue()
    
    def Normalize(text: str) -> str:
        text = text.strip().upper()
        return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
