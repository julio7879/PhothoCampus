import funciones
import persistencia

while True:
    print("\n --- PhotoCampus: Gestión de Servicios ---")
    print("1. Listar servicios")
    print("2. Agregar servicio")
    print("3. Editar servicio")
    print("4. Eliminar servicio")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")
    
    match opcion:
        
        case "1":
            if opcion == "1":
                print("\n Lista de servicios:")
                funciones.listar_servicios()

        case "2":
                print("\nAgregar nuevo servicio")
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                tipo = input("Tipo de evento: ")
                duracion = int(input("Duración (horas): "))
                funciones.agregar_servicio(nombre, precio, tipo, duracion)
                print(" Servicio agregado correctamente")

        