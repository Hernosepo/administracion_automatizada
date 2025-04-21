
from src.proyecto import Proyecto

proyecto = Proyecto()
print(proyecto.datos_proyecto["cliente"])  # Debería imprimir: None
proyecto.datos_proyecto["cliente"] = "SUBURBIA"
print(proyecto.datos_proyecto)