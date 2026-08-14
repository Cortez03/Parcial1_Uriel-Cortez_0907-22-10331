from models import Usuario
import servicios

def ejecutar():
    tickets = []
    
    # Datos base
    solicitante = Usuario(1, "Mario Rossi", "mario@edu.gt", "student")
    tecnico = Usuario(2, "Elena Torres", "elena@edu.gt", "technician")

    print("=== SISTEMA HELPDESK EDU ===")
    
    # 1. Registrar
    t1 = servicios.registrar_ticket(tickets, 101, "Error de acceso a Aula Virtual", "Software", "High", solicitante)
    print(f"Ticket #{t1.ticket_id} registrado.")

    # 2. Asignar técnico
    if servicios.asignar_tecnico(t1, tecnico):
        print(f"Técnico {tecnico.nombre} asignado exitosamente.")

    # 3. Cambiar estado
    if servicios.cambiar_estado(t1, "In Progress"):
        print(f"Nuevo estado del ticket #{t1.ticket_id}: {t1.get_estado()}")

    # 4. Listar
    print("\n--- LISTA GENERAL DE TICKETS ---")
    for t in servicios.listar_tickets(tickets):
        tec_nom = t.tecnico.nombre if t.tecnico else "N/A"
        print(f"ID: {t.ticket_id} | Título: {t.titulo} | Estado: {t.get_estado()} | Asignado: {tec_nom}")

if __name__ == "__main__":
    ejecutar()