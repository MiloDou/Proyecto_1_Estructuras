class Provider:
    def __init__(self, id: int, name: str, service: str, rating: int):
        self.id = id
        self.name = name
        self.service = service
        self.rating = rating

    def __str__(self):
        return(f"\033[1;93m   ═════════ ID: {self.id}\033[0m\n"
                f"   - Nombre: {self.name}\n"
                f"   - Tipo de Servicio: {self.service}\n"
                f"   - Calificación: {self.rating}\n")
    
    @staticmethod
    def ranking(providers):
        print('Top rated providers:')
        sorted_providers = sorted(providers, key=lambda p: p.rating, reverse=True)
        for provider in sorted_providers:
            print(provider)

    @staticmethod
    def alphabetic_orden(providers):
        print('Providers in alphabetical order:')
        sorted_providers = sorted(providers, key=lambda p: p.name)
        for provider in sorted_providers:
            print(provider)
    
    @staticmethod
    def common_services(providers):
        service_count = {}
        for provider in providers:
            if provider.service in service_count:
                service_count[provider.service] += 1
            else:
                service_count[provider.service] = 1
        result = "Common services:\n"
        for service, count in service_count.items():
            result += f"{service}: {count}\n"
        return result
    