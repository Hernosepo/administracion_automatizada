# Proyecto: Automatización Administrativa

## 🧭 Introducción

Este proyecto busca automatizar tareas administrativas repetitivas mediante scripts en Python. Está pensado para entornos donde se trabaja con múltiples proyectos que requieren estructuras de carpetas, archivos, planillas y documentación que repite datos clave como el código de proyecto, el cliente y el nombre del proyecto. Es una herramienta de productividad para reducir la carga operativa, estandarizar formatos y minimizar errores manuales.
Si bien cualquier compañía o estructura puede beneficiarse con esta automatización en este caso empezaré con un caso real en la empresa de servicios de casting que actualmente administro.

## 🎯 Objetivo General

Crear un sistema automatizado que permita generar carpetas y archivos administrativos personalizados a partir de datos clave ingresados por el usuario. A largo plazo, el sistema será modular, reutilizable y podrá contar con interfaz gráfica o web.

## ✅ Objetivos Específicos

- Generar una carpeta madre con nombre compuesto por código + cliente + proyecto.
- Crear subcarpetas predefinidas (como "TALENTO" y "PROVEEDORES").
- Generar archivos con nombres estandarizados que incluyan los datos clave.
- (Etapas futuras) Copiar desde plantillas base y rellenar campos internos automáticamente.
- Documentar el proceso, buenas prácticas y decisiones técnicas para un repositorio profesional en GitHub.

## 📦 Estructura Inicial

```text
250301SMS SUBURBIA MID SEASON/
├── TALENTO/
|    └── CONTRACTUALES/ # SE CREA LA CARPETA VACIA Y SE VAN MIGRANDO ARCHIVOS A MEDIDA QUE LLEGAN
|    |   ├── CONTRATOS/
|    |   ├── SELECCIONES/
|    |   └── SOLICITUD DE CASTING/
|    └── CIERRE/
|    |   ├── 250301SMS SUBURBIA MID SEASON CIERRE TALENTO.xlsx
|    |   └── 250301SMS SUBURBIA MID SEASON CIERRE TALENTO.numbers
|    |
|    └── ORDENES DE COMPRA Y PORTADA/
|        ├── 250301SMS SUBURBIA MID SEASON ORDEN DE COMPRA - TALENTO.xlsx
|        ├── 250301SMS SUBURBIA MID SEASON ORDEN DE COMPRA - TALENTO.numbers
|        ├── 250301SMS SUBURBIA MID SEASON PORTADA.key
|        └── 250301SMS SUBURBIA MID SEASON PORTADA.ppt
|
└── PROVEEDORES/
|    └── CIERRE/
|    |   ├── 250301SMS SUBURBIA MID SEASON CIERRE PROVEEDORES.xlsx
|    |   └── 250301SMS SUBURBIA MID SEASON CIERRE PROVEEDORES.numbers
|    |
|    └── ORDENES DE COMPRA/
|        ├── 250301SMS SUBURBIA MID SEASON ORDEN DE COMPRA - PROVEEDORES.xlsx
|        └── 250301SMS SUBURBIA MID SEASON ORDEN DE COMPRA - PROVEEDORES.numbers
|
|
└── CIERRE/
    ├── 250301SMS SUBURBIA MID SEASON CONTRATOS DIGITALIZADOS/
    ├── 250301SMS SUBURBIA MID SEASON CIERRE TALENTOS/
    └── 250301SMS SUBURBIA MID SEASON CIERRE PROVEEDORES/
```

## 🛠️ Librerías Utilizadas

- pathlib: para manipulación de archivos y carpetas
- (futuro) `openpyxl`: para editar archivos `.xlsx`
- (futuro) `python-docx`: para editar archivos `.docx`

## ⚙️ Funcionamiento del sistema

El usuario ingresará tres datos clave: código, cliente y nombre del proyecto. A partir de eso, se generará una carpeta con nombre dinámico y dentro de ella:

- Subcarpetas predefinidas
- Archivos renombrados dinámicamente
- (futuro) Archivos copiados desde plantillas base
- (futuro) Reemplazo automático de campos dentro de los archivos

## 📌 Estado actual del proyecto

Versión inicial funcional que:

- Toma inputs por variables
- Crea la carpeta principal y subcarpetas
- Genera archivos vacíos con nombres dinámicos

## 🧪 Próximos pasos sugeridos

- [ ] Añadir copia de archivos desde plantillas
- [ ] Agregar completado automático de datos en los archivos
- [ ] Modularizar el código en funciones reutilizables
- [ ] Crear estructura de carpetas del repositorio (`/src`, `/templates`, `/docs`, etc.)
- [ ] Desarrollar una interfaz mínima para facilitar el ingreso de datos

## ✍️ Autor

Hernán — Proyecto desarrollado como parte del Máster Full-Stack y orientado a tareas reales del entorno laboral.
