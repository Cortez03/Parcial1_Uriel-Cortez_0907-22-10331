from models import Ticket

def registrar_ticket(lista_tickets, t_id, titulo, cat, prio, solicitante):
    nuevo = Ticket(t_id, titulo, cat, prio, solicitante)
    lista_tickets.append(nuevo)
    return nuevo

def listar_tickets(lista_tickets):
    return lista_tickets

def buscar_ticket(lista_tickets, t_id):
    for t in lista_tickets:
        if t.ticket_id == t_id:
            return t
    return None

def asignar_tecnico(ticket, usuario_tecnico):
    if usuario_tecnico.rol == "technician":
        ticket.tecnico = usuario_tecnico
        return True
    return False

def cambiar_estado(ticket, nuevo_estado):
    return ticket.set_estado(nuevo_estado)