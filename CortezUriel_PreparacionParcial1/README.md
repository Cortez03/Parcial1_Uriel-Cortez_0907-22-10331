# Preparación Previa al Primer Parcial - Programación II
**Curso:** Programación II  
**Herramientas:** Python 3, Visual Studio Code, PlantUML  
**Proyecto Base:** HelpDesk EDU  

---

## Estructura del Repositorio

```text
CortezUriel_PreparacionParcial1/
│── 01_registro_ticket.py
│── 02_menu_helpdesk.py
│── 03_modelos.py
│── 04_modelo_helpdesk.puml
│── 04_modelos_base.py
│── 04_justificacion_relaciones.md
│── 05_helpdesk_app/
│   ├── models.py
│   ├── servicios.py
│   ├── main.py
│   └── README.md
└── README.md
```

---

## Ejercicio 1. Registro de un ticket por consola (Semana 1)

### Enunciado
Construir un primer registro usando entrada, conversión, condicionales, listas y diccionarios.

**Requisitos obligatorios:**
- Solicite número de ticket, solicitante, título, descripción, categoría y prioridad.
- Valide el número con `try/except ValueError` y rechace campos obligatorios vacíos.
- Categorías válidas: `General`, `Hardware`, `Software` y `Network`.
- Prioridades válidas: `Low`, `Medium`, `High` y `Critical`.
- Guarde el registro en un diccionario con `status` inicial `Open` y muestre un resumen con `f-strings`.

**Prueba mínima:**
Pruebe un número inválido, un campo vacío y un registro válido. El programa no debe finalizar con una excepción no controlada.

---

## Ejercicio 2. Menú modular de tickets en memoria (Semana 1)

### Enunciado
Refactorizar el registro anterior como un programa modular que mantenga varios tickets durante la ejecución.

**Requisitos obligatorios:**
- Implemente `pedir_opcion()`, `registrar_ticket()`, `listar_tickets()`, `buscar_por_solicitante()`, `mostrar_resumen()` y `ejecutar_menu()`.
- Use una lista de diccionarios y agregue registros con `append()`.
- Menú: registrar, listar, buscar por solicitante, resumen por prioridad y salir.
- Use `while`, `if/elif/else`, `for`, `len()` y comparación sin distinguir mayúsculas/minúsculas.
- Incluya `if __name__ == "__main__":` para iniciar el menú.

**Prueba mínima:**
Registre al menos tres tickets, busque uno por solicitante y muestre el conteo por prioridad antes de salir.

---

## Ejercicio 3. Modelo orientado a objetos (Semana 2)

### Enunciado
Representar usuarios y tickets mediante clases con estado, comportamiento y colecciones de objetos.

**Requisitos obligatorios:**
- Cree `Usuario` con `id`, `nombre`, `email` y `rol`; cree `Ticket` con `id`, `título`, `categoría`, `prioridad`, `solicitante`, `técnico opcional` y `estado`.
- Utilice `__init__`, `self` y `__str__` en ambas clases.
- Encapsule el estado como `_status` y cámbielo mediante `cambiar_estado()`.
- Estados válidos: `Open`, `In Progress`, `Resolved`, `Closed` y `Cancelled`.
- Implemente `asignar_tecnico(tecnico)` y valide que el rol sea `technician`.
- Cree dos usuarios y tres tickets, almacénelos en una lista de objetos e imprímalos.

**Prueba mínima:**
Asigne un técnico, cambie un ticket a `In Progress` y controle un intento de estado no permitido.

---

## Ejercicio 4. UML y relaciones del dominio HelpDesk EDU (Semanas 3 y 4)

### Enunciado
Diseñar un modelo coherente y relacionarlo con esqueletos Python, sin persistencia ni frameworks.

**Requisitos obligatorios:**
- Modele `User`, `Ticket`, `Comment`, `History` y `Article` con atributos y al menos un método relevante.
- Represente `User "1" -- "0..*"` Ticket para el solicitante y `User "0..1" -- "0..*"` Ticket para el técnico opcional.
- Represente `Ticket "1" *-- "0..*"` Comment y `Ticket "1" *-- "0..*"` History como composiciones.
- Represente `User "1" -- "0..*"` Article como asociación.
- Cree esqueletos Python consistentes con el diagrama.
- Justifique cada relación, multiplicidad y criterio de ciclo de vida.

**Prueba mínima:**
Renderice el diagrama en VS Code con PlantUML y verifique que los rombos negros estén del lado de `Ticket`.

---

## Ejercicio 5. Miniaplicación HelpDesk organizada por módulos (Semana 5 e integración)

### Enunciado
Integrar consola, modularidad, POO, relaciones y estructura de programa en una solución pequeña y ejecutable.

**Requisitos obligatorios:**
- En `models.py` coloque las clases `Usuario` y `Ticket`; no incluya el menú.
- En `servicios.py` implemente `registrar_ticket()`, `listar_tickets()`, `buscar_ticket()`, `asignar_tecnico()` y `cambiar_estado()`.
- En `main.py` implemente el menú, importe modelos y servicios, y use `if __name__ == "__main__":`.
- Trabaje con una lista de objetos `Ticket` y evite duplicar lógica.
- Incluya un flujo mínimo: crear solicitante y técnico, registrar ticket, asignarlo, cambiar su estado y listarlo.
- En `README.md` documente la estructura y el comando `python main.py`.

**Prueba mínima:**
Ejecute desde `05_helpdesk_app` y demuestre el flujo completo sin errores de importación.