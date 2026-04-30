import json
import os

archivo = "servicios.json"

def cargar_servicios():
    if not os.path.exists(archivo):
        return []
    with open(archivo, "r") as f:
        return json.load(f)

def guardar_servicios(servicios):
    with open(archivo, "w") as f:
        json.dump(servicios, f, indent=4)