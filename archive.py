from b_tree import BTree
from providers import Provider
import time
import os 
class Archive:
    def __init__(self):
        self.providers = BTree(3)
    
    def get_data(self):
        return self.providers
    
    def create_archive(self):
        print("Creando el archivo...")
        time.sleep(2)
        all_providers = self.providers.get_all_providers()
        with open('archive.txt', 'w', encoding='utf-8') as file_1:
            if not all_providers:
                file_1.write("No hay trabajadores registrados.\n")
            else:
                for provider in all_providers:
                    file_1.write(str(provider) + "\n")
                    file_1.write("    ════════════════════════════════════════\n")
                file_1.write(f'   Total de trabajadores: {len(all_providers)}\n')
                file_1.write("    ════════════════════════════════════════\n")
                file_1.write(f'   Fecha de creación: {time.strftime("%Y-%m-%d %H:%M:%S")}\n')
                file_1.write("    ════════════════════════════════════════\n")
                file_1.write(Provider.ranking(all_providers) + "\n")
                file_1.write("    ════════════════════════════════════════\n")
                file_1.write(Provider.alphabetic_orden(all_providers) + "\n")
                file_1.write("    ════════════════════════════════════════\n")
                file_1.write(Provider.common_services(all_providers) + "\n")
                file_1.write("    ════════════════════════════════════════\n")
                file_1.write("Todos los trabajadores:\n")
                for provider in all_providers:
                    file_1.write(str(provider) + "\n")
        print("Archivo 'archive.txt' creado exitosamente.")
        os.startfile('archive.txt')
