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
    print("Servicio agregado correctamente.")

def listar_servicios():
    servicios = persistencia.cargar_servicios()
    if not servicios:
        print("No hay servicios.")
        return
    for s in servicios:
        print(f"ID: {s['id']} | Nombre: {s['nombre']} | Precio: {s['precio']} | Tipo: {s['tipo_evento']} | Horas: {s['duracion_horas']}")

def editar_servicios():
    servicios = persistencia.cargar_servicios()
    
    if not servicios:
        print("Archivo vacio.")
        return

    nombre_buscar = input("Nombre del servicio a editar: ")
    encontrado = False

    for servicio in servicios:
        if servicio["nombre"].lower() == nombre_buscar.lower():
            encontrado = True
            print(f"Editando: {servicio['nombre']}")
            
            n_nombre = input(f"Nombre [{servicio['nombre']}]: ") or servicio['nombre']
            
            n_precio_raw = input(f"Precio [{servicio['precio']}]: ")
            n_precio = float(n_precio_raw) if n_precio_raw else servicio['precio']
            
            n_tipo = input(f"Tipo [{servicio['tipo_evento']}]: ") or servicio['tipo_evento']
            
            n_duracion_raw = input(f"Horas [{servicio['duracion_horas']}]: ")
            n_duracion = int(n_duracion_raw) if n_duracion_raw else servicio['duracion_horas']

            
            servicio["precio"] = n_precio
            servicio["tipo_evento"] = n_tipo
            servicio["duracion_horas"] = n_duracion
            break
    
    if encontrado:
        persistencia.guardar_servicios(servicios)
        print("Cambios guardados exitosamente.")
    else:
        print("No se encontro el nombre.")