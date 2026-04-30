import json
import os

archivo = "servicios.json"

def cargar_servicios():
    if not os.path.exists(archivo):
        return []
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def guardar_servicios(servicios):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(servicios, f, indent=4, ensure_ascii=False)