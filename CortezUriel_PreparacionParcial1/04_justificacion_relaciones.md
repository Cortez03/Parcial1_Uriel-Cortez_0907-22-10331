# Justificación de Relaciones UML - HelpDesk EDU

1. **User (1) -- (0..*) Ticket [Solicitante]:**
   - **Asociación:** Un usuario puede registrar múltiples tickets. El usuario existe independientemente de si tiene o no tickets creados.

2. **User (0..1) -- (0..*) Ticket [Técnico]:**
   - **Asociación:** Un ticket puede no tener un técnico asignado al inicio (0..1) o tener asignado exactamente a uno.

3. **Ticket (1) *-- (0..*) Comment:**
   - **Composición:** Rombo negro en `Ticket`. Un comentario no tiene razón de existir fuera de su ticket correspondiente. Si el ticket se destruye, los comentarios asociados se destruyen con él.

4. **Ticket (1) *-- (0..*) History:**
   - **Composición:** Rombo negro en `Ticket`. La bitácora de historial de cambios pertenece exclusivamente al ciclo de vida de su ticket.

5. **User (1) -- (0..*) Article:**
   - **Asociación:** Un usuario autor crea artículos de la base de conocimiento. Si el artículo se elimina, el autor sigue existiendo en el sistema.