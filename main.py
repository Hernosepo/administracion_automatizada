
from src.generador import crear_nombre_proyecto, crear_estructura_carpetas

codigo = '250301SMS'
cliente = 'SUBURBIA'
proyecto = 'MID SEASON'

nombre = crear_nombre_proyecto(codigo, cliente, proyecto)
crear_estructura_carpetas(nombre)

print(f"Proyecto creado: {nombre}")

