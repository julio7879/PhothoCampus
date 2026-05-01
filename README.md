#  PhotoCampus - Gestión de Servicios

## Introducción

PhotoCampus es una plataforma diseñada para optimizar la administración de servicios de fotografía profesional. Este sistema permite gestionar paquetes fotográficos (bodas, retratos, productos, etc.) de manera eficiente, garantizando la persistencia de datos mediante almacenamiento local en formato JSON y una colaboración robusta basada en el control de versiones con Git y GitHub.

##  Equipo de desarrollo

- Julio Ernesto Castaño Palacios  
- Zlatan Villamizar  
- Valeria Lizcano  

##  Funcionalidades

-  Listar todos los servicios registrados  
-  Agregar un nuevo servicio (se asigna ID automáticamente)  
-  Editar un servicio existente (búsqueda por nombre)  
-  Eliminar un servicio por su ID  
- Persistencia de datos en `servicios.json`

## --- PhotoCampus: Gestión de Servicios ---

1. Listar servicios
2. Agregar servicio
3. Editar servicio
4. Eliminar servicio
5. Salir

## Tecnologías utilizadas

- Python 3.x  
- Módulo `json` para persistencia  
- Módulo `os` para manejo de archivos


##  Estructura del proyecto
PhotoCampus/
├── main.py # Menú principal e interacción con el usuario
├── funciones.py # Lógica de negocio (CRUD)
├── persistencia.py # Carga y guardado de datos en JSON
├── servicios.json # Archivo de almacenamiento de servicios
└── README.md # Documentación del proyecto

 Notas
Los IDs se asignan automáticamente de forma incremental.

Si el archivo servicios.json no existe o está corrupto, el programa lo maneja correctamente.

La edición se realiza buscando por nombre (no distingue mayúsculas/minúsculas).

Al editar, si se deja un campo vacío, se conserva el valor anterior.
