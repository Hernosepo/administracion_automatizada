
from src.proyecto import Proyecto

proyecto = Proyecto()
proyecto.capturar_datos_interactivamente()
proyecto.mostrar_estado()
proyecto.crear_documento_desde_template(nombre_template="orden_compra_modelo.txt", carpeta_destino=".")
proyecto.rellenar_template_con_datos(nombre_template="orden_compra_modelo.txt")
proyecto.crear_estructura_carpetas()