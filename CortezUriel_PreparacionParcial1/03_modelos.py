class Usuario:
    def __init__(self, id_usr, nombre, email, rol):
        self.id_usr = id_usr
        self.nombre = nombre
        self.email = email
        self.rol = rol.lower()

    def __str__(self):
        return f"Usuario({self.id_usr}, {self.nombre}, Rol: {self.rol})"

class Ticket:
    ESTADOS_VALIDOS = ["Open", "In Progress", "Resolved", "Closed", "Cancelled"]

    def __init__(self, ticket_id, titulo, categoria, prioridad, solicitante):
        self.ticket_id = ticket_id
        self.titulo = titulo
        self.categoria = categoria
        self.prioridad = prioridad
        self.solicitante = solicitante
        self.tecnico = None
        self._status = "Open"

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in self.ESTADOS_VALIDOS:
            self._status = nuevo_estado
            print(f"Estado del Ticket {self.ticket_id} cambiado a: {self._status}")
        else:
            print(f"Error: Estado '{nuevo_estado}' no es válido.")

    def asignar_tecnico(self, tecnico):
        if isinstance(tecnico, Usuario) and tecnico.rol == "technician":
            self.tecnico = tecnico
            print(f"Técnico {tecnico.nombre} asignado al Ticket {self.ticket_id}.")
        else:
            print("Error: El usuario asignado debe tener el rol 'technician'.")

    def __str__(self):
        tec_nombre = self.tecnico.nombre if self.tecnico else "Sin asignar"
        return f"Ticket #{self.ticket_id}: '{self.titulo}' | Solicitante: {self.solicitante.nombre} | Técnico: {tec_nombre} | Estado: {self._status}"

if __name__ == "__main__":
    u1 = Usuario(1, "Ana Gómez", "ana@edu.gt", "student")
    u2 = Usuario(2, "Carlos López", "carlos@edu.gt", "technician")

    t1 = Ticket(101, "Fallo de conexión WiFi", "Network", "High", u1)
    t2 = Ticket(102, "Instalación de Python", "Software", "Medium", u1)
    t3 = Ticket(103, "Teclado no funciona", "Hardware", "Low", u1)

    lista_tickets = [t1, t2, t3]

    t1.asignar_tecnico(u2)
    t1.cambiar_estado("In Progress")
    t1.cambiar_estado("InvalidState")

    print("\n--- ESTADO DE TICKETS ---")
    for t in lista_tickets:
        print(t)