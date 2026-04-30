import persistencia

def agregar_servicio(nombre, precio, tipo_evento, duracion):
    servicios = persistencia.cargar_servicios()
    nuevo_id = max([s["id"] for s in servicios], default=0) + 1
    
    nuevo = {
        "id": nuevo_id,
        "nombre": nombre,
        "precio": precio,
        "tipo_evento": tipo_evento,
        "duracion_horas": duracion
    }
    
    servicios.append(nuevo)
    persistencia.guardar_servicios(servicios)
    

def listar_servicios():
    servicios = persistencia.cargar_servicios()
    for s in servicios:
        print(s)