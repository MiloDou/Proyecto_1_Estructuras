class Provider:
    def __init__(self, id: int, name: str, service: str, rating: int):
        self.id = id
        self.name = name
        self.service = service
        self.rating = rating

    def __str__(self):
        return(f"  ═════════ID: {self.id}\n   - Nombre: {self.name}\n   - Tipo de Servicio: {self.service}   - Calificación: {self.rating}")
    
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
    