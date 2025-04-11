
from src.generador import crear_nombre_proyecto, crear_estructura_carpetas, crear_nombre_archivo

codigo = '250301SMS'
cliente = 'SUBURBIA'
proyecto = 'MID SEASON'
fecha = "2025-04-09"
tipo_archivo = "Orden de Compra"

nombre_proyecto = crear_nombre_proyecto(codigo, cliente, proyecto)
crear_estructura_carpetas(nombre_proyecto)

nombre_archivo = crear_nombre_archivo(codigo,cliente,proyecto,tipo_archivo,fecha)

print(f"Proyecto creado: {nombre_proyecto}")
print(f"Nombre de Archivo {nombre_archivo}")
