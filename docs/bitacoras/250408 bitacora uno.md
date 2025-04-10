# Bitácora

## Día 1 - 08/04/25

- Realizo un pequeño manual que consta de:

  - Pequeña introducción
  - Objetivos
    - Generales
    - Específicos
  - Defino una estructura de carpetas y archivos a crear durante el proceso
  - Investigo, evalúo y determino utilizar:
    - Pathlib sobre OS por:
      - legibilidad para leer el código
      - estilo más orientado a objetos
    - Dejo para investigar más adelante librerías que:
      - Permitan editar docs Office
      - Permitan editar docs IOS
  - Describo primeros pasos a completar como generar las funciones que permitan crear carpetas y archivos vacíos.

- Primeras líneas de código, archivos y rutas:

  - Creo carpetas y rutas para el desarrollo:
    - `ADMINISTRACION AUTOMATIZADA/administracion_automatizada`
      - Archivos `main.py` y `generador.py`
  - Funciones archivo generador:
    - `crear_nombre_proyecto(codigo, cliente, proyecto)`
      - Esta función toma las variables que juntas forman el nombre del proyecto.
      - Concateno strings para generarlo
    - `crear_estructura_carpetas(nombre_proyecto, base_dir="./")`
      - Esta función debe crear carpetas y subcarpetas para generar la estructura deseada con los parámetros del proyecto establecidos en la función anterior.
      - Si la carpeta ya existe se debe obviar
      - Utilizo Pathlib (`mkdir`, `exist_ok=True`)
    - `crear_estructura_desde_diccionario(estructura, ruta_base)`
      - Esta función recorre un diccionario que representa una estructura de carpetas y crea cada carpeta en el sistema, partiendo desde una ruta base.
      - `estructura` es el diccionario creado anteriormente
      - `ruta_base` es un objeto de Pathlib que representa la carpeta desde la que hay que empezar a construir

- Código archivo `main.py`:

  - Genero las variables a ingresar para generar nombres de archivos
  - Creo variable para llamar a las funciones
  - Con un print me aseguro de que me devuelva el string de las variables

- Próximo paso:
  - Empezar a probar las creaciones de carpetas con archivos vacíos
