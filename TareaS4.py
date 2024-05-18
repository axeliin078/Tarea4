Tareas = {}

Tareas["1"] = {"nombre": "Estudiar", "descripcion": "Ver las clases de Ciencia de Datos para entender puntos", "estado": "En progreso"}
Tareas["2"] = {"nombre": "Organizar la habitación", "descripcion": "Limpiar el piso, organizar la ropa, cambiar las sabanas", "estado": "Completado"}
Tareas["3"] = {"nombre": "Ver una serie", "descripcion": "Empezar una serie de 12 capitulos", "estado": "Pendiente"}

print("Tareas por hacer: ")
for id, tarea in Tareas.items():
    print(f"ID: {id}, Tarea: {tarea}")

tarea_eliminada = Tareas.pop("2")
print("\nTarea completada:", tarea_eliminada)

print("\nTareas restantes:")
for id, tarea in Tareas.items():
    print(f"ID: {id}, Tarea: {tarea}")