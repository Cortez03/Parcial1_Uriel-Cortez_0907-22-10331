class Usuario:
    def __init__(self, id_usr, nombre, email, rol):
        self.id_usr = id_usr
        self.nombre = nombre
        self.email = email
        self.rol = rol.lower()

class Ticket:
    def __init__(self, ticket_id, titulo, categoria, prioridad, solicitante):
        self.ticket_id = ticket_id
        self.titulo = titulo
        self.categoria = categoria
        self.prioridad = prioridad
        self.solicitante = solicitante
        self.tecnico = None
        self._status = "Open"

    def set_estado(self, nuevo_estado):
        estados = ["Open", "In Progress", "Resolved", "Closed", "Cancelled"]
        if nuevo_estado in estados:
            self._status = nuevo_estado
            return True
        return False

    def get_estado(self):
        return self._status