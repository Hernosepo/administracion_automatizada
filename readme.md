# 📁 Automatización Administrativa

Automatización de estructuras administrativas a partir de datos clave del proyecto.

Este proyecto genera de forma automática carpetas y archivos base (como README.txt) para organizar proyectos administrativos, a partir de un código, cliente y nombre. Está pensado para facilitar tareas repetitivas y mantener la organización del trabajo profesional.

---

## 🎯 Objetivos

### Generales:

- Optimizar el tiempo dedicado a tareas administrativas repetitivas.
- Mejorar la organización de carpetas y archivos por proyecto.

### Específicos:

- Generar nombres de proyectos automáticamente.
- Crear estructuras de carpetas jerárquicas a partir de un diccionario base.
- Incluir archivos `README.txt` en cada carpeta creada.

---

## 🛠 Tecnologías utilizadas

- Python 3.x
- `pathlib` para manejo de rutas
- Git + GitHub para control de versiones
- GitHub Desktop como interfaz visual

---

## 🗂 Estructura generada (ejemplo)

(CODIGO DE PROYECTO) (CLIENTE) (NOMBRE DE PROYECTO)/
        ├── TALENTO/
        │ ├── CONTRACTUALES/
        │ ├── CIERRE TALENTO/
        │ └── ORDENES DE COMPRA Y PORTADA TALENTO/
        ├── PROVEEDORES/
        │ ├── CIERRE PROVEEDORES/
        │ └── ORDENES DE COMPRA PROVEEDORES/
        └── CIERRE GENERAL/

---

## 🚀 ¿Cómo usarlo?

1. Cloná este repositorio
2. Ejecutá `main.py` para probar con datos ejemplo
3. Revisá las carpetas creadas en tu sistema local

(⚠️ Se recomienda tener Python 3.9+ instalado)

---

## 📚 Recursos útiles

- 📖 [Glosario técnico](./glosario.md)
- 🗒️ [Bitácora de desarrollo](./docs/bitacoras/250408%20bitacora%20uno.md)

---

## 🚧 Estado del proyecto

🔨 **MVP funcional**  
📂 Estructura jerárquica y archivos `README.txt` ya generados  
📌 Próximo paso: agregar plantillas editables y copiado automático de archivos base

---

## 👤 Autor

Desarrollado por [@Hernosepo](https://github.com/Hernosepo)

---

## 📝 Licencia

Este proyecto está bajo licencia MIT. Ver archivo `LICENSE`.
