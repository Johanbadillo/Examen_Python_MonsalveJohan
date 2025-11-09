<div align="center">

# Gestor de Cafetería CampusLands  
**Sistema CRUD para Inventario y Gastos**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)
![CRUD](https://img.shields.io/badge/CRUD-28A745?style=for-the-badge&logo=crud&logoColor=white)

---

**JOHAN MONSALVE**  

![CampusLands • Cajasan 2025](https://img.shields.io/badge/CampusLands_%E2%80%A2_Cajasan_2025-FD7E14?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxIiBoZWlnaHQ9IjEiPjwvc3ZnPg==&labelColor=E65100)
![ruta](https://img.shields.io/badge/RUTA-Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white)

</div>

---

## Descripción del Proyecto

**Gestor de Cafetería CampusLands** es un **sistema de gestión de inventario y gastos** desarrollado en **Python**, diseñado para optimizar el control de:

- Ingredientes  
- Categorías de hamburguesas  
- Chefs  
- Costos asociados  

> **Operaciones CRUD completas** (Crear, Leer, Actualizar, Eliminar) sobre todos los módulos.  
> **Datos persistentes en archivos JSON** – ¡Nunca pierdas tu inventario!

---

## Funcionalidades

| Módulo | Acciones Disponibles |
|-------|------------------------|
| **Ingredientes** | Registrar, ver, actualizar, eliminar |
| **Categorías** | Gestionar tipos de hamburguesas |
| **Chefs** | Control de personal y asignaciones |
| **Gastos** | Seguimiento por ítem y período |

```mermaid
graph TD
    A[Menú Principal] --> B[Ingredientes]
    A --> C[Categorías]
    A --> D[Chefs]
    A --> E[Gastos]
    B --> B1[CRUD]
    D --> D1[CRUD]
    E --> E1[CRUD]
    C --> C1[CRUD]
```
# 🛠️ Tecnologías Usadas

| Tecnología     | Uso                              |
|----------------|----------------------------------|
| **Python 3**         | Lógica, menús y operaciones CRUD        |
| **JSON**      | Almacenamiento persistente (ingredientes.json, categorias.json, etc.)           |
| **Módulos nativos**     | json, datetime         |


> *100% estático – sin dependencias externas*

## ⚙️ Instalación y Uso

Sigue estos pasos para ejecutar el proyecto localmente🧑‍💻👇:

```bash
# 1️⃣ Clonar el repositorio
git clone https://github.com/Johanbadillo/Examen_Python_MonsalveJohan.git

# 2️⃣ Entrar al directorio
cd Examen_Python_MonsalveJohan

# 3️⃣ Ejecutar el programa
python3 Examen_Python_MonsalveJohan.py
```


> *Archivos JSON generados automáticamente al primer uso*


## 📁 Estructura del proyecto
```
📁 Examen_Python_MonsalveJohan/
├── 📁 Data/
│   ├── data.json
│   ├── dataCategorias.json
│   ├── dataChefs.json
│   └── logs.json
├── 📁 Funciones/
│   ├── funciones.py
│   ├── funcionesJson.py
│   └── funcionesMensajes.py
├── Examen_Python_MonsalveJohan.py    Programa principal
├── LICENSE
└── README.md
```

## Ejemplo de Uso (Consola)
```
=== GESTOR DE CAFETERÍA CAMPUSLANDS ===
1. Ingredientes
2. Categorías
3. Chefs
4. Gastos
5. Salir
> 1
> 1. Registrar nuevo ingrediente
Nombre: Pan
Costo: 1500
Stock: 50
[Success] Ingrediente registrado!
```

## Explicación Técnica

Este sistema implementa el **patrón CRUD** sobre múltiples entidades relacionadas:

- **Persistencia:** Cada módulo guarda su estado en un archivo JSON independiente
- **Validación:** Entradas numéricas, nombres únicos, stock positivo
- **Modularidad:** Funciones separadas por responsabilidad
- **Interfaz clara:** Menús anidados y mensajes de confirmación


## 👥 Autor

<div align="center">

| 🧑‍💻 Nombre | 🎯 Rol | 🔗 GitHub |
|--------|-----|--------|
| **Johan Monsalve** | ⚙️ Python Developer | [@Johanbadillo](https://github.com/Johanbadillo) |

</div>

---

<div align="center">

**💖 ¡Optimiza tu cafetería, un ingrediente a la vez! 💖**  
**CampusLands • Cajasan • 2025**

</div>
