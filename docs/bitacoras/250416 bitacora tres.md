**Día 3 - 16/04/25**

- 🎯 **Objetivo**: Capturar datos del proyecto para volcarlos en los templates.

  - Decido ingresar datos por consola para facilitar el testeo rápido.

- 🧠 **Diccionario de proyecto**:

  - Creo el archivo `diccionario_proyecto.py` donde defino un diccionario estructurado en bloques de información.
  - Bloques actuales:
    - Datos generales
    - Términos contractuales
    - Presupuestos
    - Personajes
    - Fechas importantes
    - Información técnica
    - Extras
  - Incluyo comentarios sobre posibles tipos de datos como guía para futuro input validado o generación de formularios.

- ⚙️ **Captura de datos**:

  - Creo el archivo `captura.py` con una función que itera sobre los bloques y campos, mostrando prompts por consola y guardando los valores en una copia del diccionario original (`deepcopy` importado desde `copy` en `main.py`).
  - Uso loops `for` anidados para recorrer claves y mostrar títulos formateados.

- 🧩 **Dificultades técnicas**:

  - El manejo del `PYTHONPATH` fue un desafío importante para poder importar entre archivos correctamente.
    - Aprendí que la ubicación relativa del archivo que ejecuta el script afecta la resolución de módulos.
    - Incorporé un archivo `__init__.py` en el módulo `src` para habilitar el flujo de importaciones absolutas.

- 🔜 **Próximos pasos**:
  - Automatizar el llenado de templates a partir de los datos capturados.
  - Crear un archivo `run.py` que funcione como punto de entrada al proyecto.
