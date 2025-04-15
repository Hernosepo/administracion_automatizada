
from pathlib import Path
from src.generador import (
    crear_nombre_proyecto,
    crear_estructura_carpetas,
    crear_nombre_archivo,
    copiar_archivo_modelo
)

codigo = '250301SMS'
cliente = 'SUBURBIA'
proyecto = 'MID SEASON'
fecha = "2025-04-09"
tipo_archivo = "Orden de Compra"

nombre_proyecto = crear_nombre_proyecto(codigo, cliente, proyecto)
crear_estructura_carpetas(nombre_proyecto, base_dir=Path(__file__).parent)

nombre_archivo = crear_nombre_archivo(codigo, cliente, proyecto, tipo_archivo, fecha)

origen = Path(__file__).parent / 'templates' / 'plantilla.xlsx'
destino = Path(nombre_proyecto) / 'TALENTO' / 'ORDENES DE COMPRA Y PORTADA TALENTO'

copiar_archivo_modelo(origen, destino, nombre_archivo)

print(f"Proyecto creado: {nombre_proyecto}")
print(f"Nombre de Archivo: {nombre_archivo}")