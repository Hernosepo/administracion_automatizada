# 📚 Glosario Técnico – Proyecto Automatización Administrativa

## 🧱 Estructura y organización

- **Proyecto modular**: forma de organizar el código en archivos separados (módulos) según su función.
- **Jerarquía de carpetas**: estructura en árbol donde cada carpeta puede contener subcarpetas.
- **Diccionario de estructura**: representación de esa jerarquía usando `dict` en Python, con claves como nombres de carpetas y valores como subniveles.

## 📁 Python – Módulos y herramientas usadas

- **`pathlib`**: módulo moderno para manejar rutas de archivos y carpetas. Más legible y orientado a objetos que `os`.
  - `Path(...)`: crea una ruta.
  - `/`: operador sobrecargado para unir rutas.
  - `.mkdir()`: crea carpetas.
  - `.touch()`: crea archivos vacíos.
  - `.write_text(...)`: escribe texto en archivos.
- **`shutil`** _(planificado)_: módulo para copiar archivos.
  - `shutil.copy()`: copia archivos de una ruta a otra.

## 🧠 Programación general

- **Recursividad**: técnica donde una función se llama a sí misma para recorrer estructuras jerárquicas como diccionarios anidados.
- **Funciones**: bloques de código reutilizables. Cada función tiene un propósito claro (`crear_nombre_proyecto`, `crear_estructura_carpetas`, etc).
- **Parámetros por defecto**: como `base_dir="./"` en una función, que permite usar un valor si no se pasa ninguno.
- **Importación**: traer funciones de un archivo a otro con `from ... import ...`.

## 🛠️ Archivos y ejecución

- **`main.py`**: archivo principal ejecutable del proyecto. Orquesta el uso de las funciones del módulo.
- **`generador.py`**: archivo que contiene funciones reutilizables.
- **`README.txt` (por carpeta)**: archivo generado dentro de cada carpeta como referencia o placeholder.
- **`README.md` (del proyecto)**: archivo explicativo principal, pensado para GitHub.
- **`.gitignore`**: archivo que indica a Git qué archivos no debe incluir (por ejemplo, carpetas temporales, archivos `.DS_Store` en Mac, etc).

## 🧩 Conceptos de automatización aplicada

- **MVP (Minimum Viable Product)**: versión mínima funcional del sistema.
- **Plantillas base** (futuro): archivos `.xlsx`, `.docx`, etc. que se copiarán a las carpetas creadas para completarse automáticamente.
- **Placeholder de datos**: campos como `<<CLIENTE>>` dentro de un documento que luego serán reemplazados por datos reales.

## 💬 Utilidades prácticas

- **Visual feedback**: uso de `print()` para ver en consola el avance del proceso.
- **Hardcodeo**: valores escritos directamente en el código (por ahora usamos `"250301SMS"`, `"SUBURBIA"`...), que más adelante pueden volverse inputs o variables dinámicas.
- **Escalabilidad**: diseño del proyecto pensado para poder crecer en funcionalidades sin reescribir todo.
