# 🗂️ Automatización Administrativa

Proyecto personal desarrollado para demostrar aprendizajes técnicos en Python, con enfoque en automatización de tareas administrativas repetitivas.  
Su objetivo es **generar estructuras de carpetas y archivos base a partir de datos clave de un proyecto**, reduciendo tiempos operativos y garantizando orden documental.

Este repositorio está organizado para reflejar tanto el avance funcional como la transición hacia una **arquitectura orientada a objetos**.

---

## 🚀 Estado del Proyecto

| Versión | Estado        | Enfoque                    |
|---------|---------------|----------------------------|
| v1      | ✅ Funcional   | Scripts modulares en Python |
| v2      | 🚧 En desarrollo | Programación Orientada a Objetos |

---

## 🧠 ¿Qué genera este proyecto?

A partir del ingreso de datos como código, cliente, nombre del proyecto y fecha, se genera automáticamente:

- Una carpeta raíz del proyecto
- Subcarpetas por área (TALENTO, PROVEEDORES, etc.)
- Carpetas de cierre, contratos, órdenes de compra, etc.
- Archivos base `.txt` (README) y archivos modelo `.xlsx`, `.numbers`, etc.

Ejemplo de estructura:

```
📁 250301SMS SUBURBIA MID SEASON
├── TALENTO/
│   ├── CONTRACTUALES/
│   ├── ORDENES DE COMPRA Y PORTADA/
│   └── CIERRE TALENTO/
├── PROVEEDORES/
│   └── ORDENES DE COMPRA/
└── CIERRE GENERAL/
```

---

## 🛠️ Tecnologías utilizadas

- Python 3.10+
- `pathlib` para gestión de rutas
- `shutil` para copiado de archivos modelo
- Estructura modular escalable
- En desarrollo: implementación con clases

---

## 🧭 Plan a Futuro

- ✅ Captura de datos desde consola
- ✅ Generación de estructura de carpetas base
- ✅ Inclusión de archivos `README.txt` y plantillas modelo
- 🔄 Transición a POO (Programación Orientada a Objetos)
- 🔜 Interfaz visual simple (GUI o web)
- 🔜 Soporte para más formatos y editores (`.docx`, `.pdf`, `.key`)

---

## 📒 Bitácoras

La evolución del proyecto se documenta día a día:

📂 [`docs/bitacoras`](./docs/bitacoras)

---

## 📘 Glosario Técnico

Recursos y conceptos clave organizados para consulta:

📂 [`docs/glosarios_tecnicos`](./docs/glosarios_tecnicos)

---

## 👤 Autor

Desarrollado por [@Hernosepo](https://github.com/Hernosepo)  
Amante del orden, las estructuras claras y la automatización con propósito.

---

## 📁 Versiones

Este repositorio utiliza una carpeta `versiones/` donde se organiza:

```
📁 versiones/
├── v1-funcional/
└── v2-orientado-objetos/
```

Cada versión tiene su propio README interno.

---