def pedir_opcion():
    try:
        return int(input("\nSeleccione una opción: "))
    except ValueError:
        return -1

def registrar_ticket(tickets):
    try:
        t_id = int(input("ID Ticket: "))
    except ValueError:
        print("Error: ID numérico inválido.")
        return

    solicitante = input("Solicitante: ").strip()
    titulo = input("Título: ").strip()
    
    if not solicitante or not titulo:
        print("Error: El solicitante y el título son obligatorios.")
        return

    prioridades = ["Low", "Medium", "High", "Critical"]
    prioridad = input("Prioridad (Low, Medium, High, Critical): ").strip().capitalize()
    if prioridad not in prioridades:
        prioridad = "Low"

    ticket = {
        "id": t_id,
        "solicitante": solicitante,
        "titulo": titulo,
        "prioridad": prioridad,
        "status": "Open"
    }
    tickets.append(ticket)
    print("Ticket registrado exitosamente.")

def listar_tickets(tickets):
    if not tickets:
        print("No hay tickets registrados.")
        return
    for t in tickets:
        print(f"[{t['id']}] {t['titulo']} - Solicitante: {t['solicitante']} | Prioridad: {t['prioridad']} | Estado: {t['status']}")

def buscar_por_solicitante(tickets):
    busqueda = input("Ingrese el nombre del solicitante a buscar: ").strip().lower()
    encontrados = [t for t in tickets if busqueda in t['solicitante'].lower()]
    if encontrados:
        for t in encontrados:
            print(f"[{t['id']}] {t['titulo']} ({t['status']})")
    else:
        print("No se encontraron tickets para el solicitante indicado.")

def mostrar_resumen(tickets):
    conteo = {"Low": 0, "Medium": 0, "High": 0, "Critical": 0}
    for t in tickets:
        p = t.get("prioridad")
        if p in conteo:
            conteo[p] += 1
    print(f"\nTotal de tickets: {len(tickets)}")
    for prio, cantidad in conteo.items():
        print(f" Prioridad {prio}: {cantidad}")

def ejecutar_menu():
    tickets = []
    while True:
        print("\n=== HELPDESK EDU - MENÚ ===")
        print("1. Registrar ticket")
        print("2. Listar tickets")
        print("3. Buscar por solicitante")
        print("4. Resumen por prioridad")
        print("5. Salir")
        
        opc = pedir_opcion()
        if opc == 1:
            registrar_ticket(tickets)
        elif opc == 2:
            listar_tickets(tickets)
        elif opc == 3:
            buscar_por_solicitante(tickets)
        elif opc == 4:
            mostrar_resumen(tickets)
        elif opc == 5:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    ejecutar_menu()