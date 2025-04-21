
import shutil
from pathlib import Path


# Funcion crea string unificado del nombre del proyecto
def crear_nombre_proyecto(codigo,cliente,proyecto):

    # Concatenacion de los strings, devuelve: CODIGO CLIENTE PROYECTO
    nombre_completo_proyecto = f"{codigo} {cliente} {proyecto}"
    return nombre_completo_proyecto

def crear_nombre_archivo(codigo,cliente,proyecto,tipo_archivo,fecha):
    nombre_completo_archivo = f"{codigo}_{cliente.upper().strip()}_{proyecto.upper().replace(' ', '')}_{tipo_archivo.upper().replace(' ', '')}_{fecha.replace('-', '')}.txt"
    return nombre_completo_archivo


# Funcion para crear estructura de carpetas
def crear_estructura_carpetas(nombre_proyecto, base_dir="./"):
    carpeta_principal = Path(base_dir) / nombre_proyecto
    carpeta_principal.mkdir(parents=True, exist_ok=True)

    # Diccionario para arbol de carpetas
    estructuras = {
        'TALENTO': {
            'CONTRACTUALES': {
                'CONTRATOS': {},
                'SOLICITUDES DE CASTING': {},
                'SELECCION DE TALENTO': {},
            },
            'CIERRE TALENTO':{},
            'ORDENES DE COMPRA Y PORTADA TALENTO': {},
        },
        'PROVEEDORES':{
            'CIERRE PROVEEDORES': {},
            'ORDENES DE COMPRA PROVEEDORES': {},
        },    
        'CIERRE GENERAL': {},
    }
    crear_estructura_desde_diccionario(estructuras, carpeta_principal)

# Función toma diccionario y ruta para crear arbol de carpetas
def crear_estructura_desde_diccionario(estructura, ruta_base):
   for nombre_carpeta, subestructura in estructura.items():
       nueva_ruta = ruta_base / nombre_carpeta
       nueva_ruta.mkdir(exist_ok=True)

       # Crear README.txt dentro de cada carpeta
       readme = nueva_ruta / "README.txt"
       readme.write_text(f"Carpeta: {nombre_carpeta}\nProyecto: {ruta_base.name}\n")
       
       # is instance para verificar tipo
       if isinstance(subestructura, dict):
          crear_estructura_desde_diccionario(subestructura, nueva_ruta)

# Funcion para empezar a trabajar el copiado de templates a carpetas creadas
def copiar_archivo_modelo(origen, destino, nuevo_nombre):
    origen_path = Path(origen)
    destino_path = Path(destino) / nuevo_nombre
    shutil.copy(origen_path, destino_path)