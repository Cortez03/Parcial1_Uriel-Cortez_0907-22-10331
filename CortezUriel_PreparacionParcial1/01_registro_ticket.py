def registrar_ticket():
    CATEGORIAS_VALIDAS = ["General", "Hardware", "Software", "Network"]
    PRIORIDADES_VALIDAS = ["Low", "Medium", "High", "Critical"]

    print("--- REGISTRO DE TICKET ---")
    try:
        ticket_id = int(input("Ingrese número de ticket: "))
    except ValueError:
        print("Error: El número de ticket debe ser un valor entero numérico.")
        return

    solicitante = input("Solicitante: ").strip()
    titulo = input("Título: ").strip()
    descripcion = input("Descripción: ").strip()

    if not solicitante or not titulo or not descripcion:
        print("Error: Los campos solicitante, título y descripción son obligatorios.")
        return

    categoria = input(f"Categoría {CATEGORIAS_VALIDAS}: ").strip().capitalize()
    if categoria not in CATEGORIAS_VALIDAS:
        print("Error: Categoría no válida.")
        return

    prioridad = input(f"Prioridad {PRIORIDADES_VALIDAS}: ").strip().capitalize()
    if prioridad not in PRIORIDADES_VALIDAS:
        print("Error: Prioridad no válida.")
        return

    ticket = {
        "id": ticket_id,
        "solicitante": solicitante,
        "titulo": titulo,
        "descripcion": descripcion,
        "categoria": categoria,
        "prioridad": prioridad,
        "status": "Open"
    }

    print("\n--- TICKET REGISTRADO CON ÉXITO ---")
    print(f"ID: {ticket['id']} | Solicitante: {ticket['solicitante']}")
    print(f"Título: {ticket['titulo']} | Categoría: {ticket['categoria']}")
    print(f"Prioridad: {ticket['prioridad']} | Estado: {ticket['status']}")

if __name__ == "__main__":
    registrar_ticket()