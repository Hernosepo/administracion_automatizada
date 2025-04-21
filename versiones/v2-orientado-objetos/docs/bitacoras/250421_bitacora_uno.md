## 📓 Bitácora – Día 4 (21/04/25)

### 🔧 Actividades realizadas

- Implementé el método `rellenar_template_con_datos()` en la clase `Proyecto`, que permite:
  - Leer una plantilla `.txt` con campos marcados como `{{campo}}`
  - Unificar todos los bloques de datos del proyecto en un solo diccionario
  - Reemplazar dinámicamente los placeholders por los datos reales capturados
  - Guardar el archivo final en una ubicación determinada

- Corregí errores de importación, ejecución y doble creación de archivos
- Verifiqué que el archivo `orden_compra_modelo.txt` tuviera los placeholders correctos
- Probé exitosamente el reemplazo automático desde consola
- Se creó correctamente un archivo nuevo con el contenido reemplazado por los datos del proyecto

### ✅ Resultados

- El sistema ahora permite automatizar no solo la creación de carpetas y copias de documentos, sino también el completado dinámico de archivos `.txt` desde plantillas.
- Todo el flujo es 100% orientado a objetos.

### 🔜 Próximos pasos

- Implementar reemplazo dinámico en archivos `.xlsx` utilizando `openpyxl`
- Documentar y organizar rutas destino de cada tipo de documento generado
- Comenzar a definir un archivo `run.py` que centralice la ejecución
- Continuar bitácora y glosario para cierre de versión v2