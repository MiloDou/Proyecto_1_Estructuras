from b_tree import BTree
from providers import Provider
import time
import os 
from excepts import Excepts
class Archive:
    def is_empty(self):
        """Return True if there are no providers in the tree."""
        return len(self.providers.get_all_providers()) == 0
    def __init__(self):
        self.providers = BTree(3)
    
    def get_data(self):
        return self.providers
    
    def create_archive(self):
        Excepts.animate("    Creando el archivo...", delay=0.1)
        all_providers = self.providers.get_all_providers()
        with open('archive.csv', 'w', encoding='utf-8') as file_1:
            if not all_providers:
                file_1.write("No hay trabajadores registrados.\n")
            else:
                file_1.write("LISTA DE TRABAJADORES\n")
                file_1.write("="*40 + "\n")
                for provider in all_providers:
                    file_1.write(str(provider) + "\n")
                    file_1.write("-"*40 + "\n")
                file_1.write(f"Total de trabajadores: {len(all_providers)}\n")
                file_1.write(f"Fecha de creación: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        print("\n\033[1;92m    Archivo 'archive.csv' creado exitosamente.\033[0m\n")
