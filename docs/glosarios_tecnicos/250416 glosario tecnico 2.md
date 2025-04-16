# 📘 Glosario Técnico – Día 3 (16/04/25)

Este glosario resume los términos y conceptos clave trabajados durante la jornada de desarrollo del 16 de abril de 2025, en el marco del proyecto **Automatización Administrativa**.

---

### 📁 diccionario_proyecto
Archivo `.py` que contiene una estructura base con todos los campos relevantes de un proyecto, organizados por bloques temáticos. Se usa como plantilla para captura y gestión de datos.

### 📄 deepcopy
Función importada desde el módulo `copy` de Python que permite clonar estructuras de datos (como diccionarios) sin que los cambios afecten al original. Ideal para trabajar con formularios y plantillas base.

### 🖥 captura.py
Archivo donde se implementa una función interactiva que recorre el diccionario del proyecto y permite al usuario completar datos campo por campo desde consola.

### 🔄 Loop for anidado
Estructura usada para recorrer bloques y subcampos del diccionario, lo que permite iterar secciones dinámicamente sin codificar cada campo a mano.

### 🧠 PYTHONPATH
Variable de entorno que define las rutas donde Python busca módulos y paquetes. Fue necesario entenderla para que las importaciones entre archivos funcionen correctamente.

### 🧩 __init__.py
Archivo especial de Python que declara que una carpeta debe ser tratada como un paquete. Su presencia en `src/` permitió realizar importaciones absolutas dentro del proyecto.

### 🔗 Importación absoluta
Forma de importar un módulo usando su ruta completa desde la raíz del paquete. Por ejemplo:
```python
from administracion_automatizada.src.generador import crear_nombre_archivo
```
A diferencia de importaciones relativas, las absolutas son más estables en estructuras profesionales.

### 🚀 run.py
Archivo que funcionará como punto de entrada del proyecto. Se ubicará en la raíz y llamará a `main.run()`, garantizando que todo el sistema se ejecute desde un único lugar controlado.

### 🧭 Punto de entrada
El archivo que lanza el sistema y organiza el flujo principal. Tener uno solo (como `run.py`) mejora la claridad, mantenibilidad y reduce errores de ruta.

---

Este glosario queda abierto para ser ampliado conforme evolucione el sistema.
