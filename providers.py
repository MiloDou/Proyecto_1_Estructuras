class Provider:
    def __init__(self, id: int, name: str, service: str, rating: int):
        self.id = id
        self.name = name
        self.service = service
        self.rating = rating

    def __str__(self):
        
        return(f"  ═════════ID: {self.id}\n   - Nombre: {self.name}\n   - Tipo de Servicio: {self.service}   - Calificación: {self.rating}")
    