# ⛏ MineSys — Sistema de Gestión Minera

Sistema de escritorio desarrollado en Python con interfaz gráfica Tkinter para la gestión de operaciones mineras. Permite administrar yacimientos, maquinaria, empleados y registros de seguridad.

---

## 📋 Requisitos previos

- Python 3.8 o superior
- pip

---

## ⚙️ Instalación

**1. Clona el repositorio:**
```bash
git clone https://github.com/tu_usuario/minesys.git
cd minesys
```

**2. Instala las dependencias:**
```bash
pip install tkcalendar Pillow openpyxl reportlab
```

**3. Ejecuta la aplicación:**
```bash
python app.py
```

La base de datos `minesys.db` se crea automáticamente en la carpeta `models/` al primer inicio.

---

## 📁 Estructura del proyecto

```
minesys/
├── app.py              ← Archivo principal (ejecutar este)
├── favicon.ico         ← Se genera automáticamente al iniciar
├── README.md
└── models/
    └── minesys.db      ← Base de datos SQLite (se crea automáticamente)
```

---

## 🚀 Funcionalidades

### Módulos
| Módulo        | Descripción                                      |
|---------------|--------------------------------------------------|
| Yacimientos   | Registro y gestión de yacimientos mineros        |
| Maquinaria    | Control de equipos y maquinaria pesada           |
| Empleados     | Gestión del personal de la operación             |
| Seguridad     | Registro de incidentes y acciones de seguridad   |

### Características por módulo
- ✅ **CRUD completo** — Guardar, Actualizar, Eliminar y visualizar registros
- ✅ **Exportar a Excel** — Genera archivo `.xlsx` con los datos de cada módulo
- ✅ **Exportar a PDF** — Genera reporte `.pdf` con formato profesional
- ✅ **Gestión de imágenes** — Soporte JPG, PNG y GIF con preview (Yacimientos y Empleados)
- ✅ **Selector de fechas** — Calendario flotante con `tkcalendar`
- ✅ **Validaciones** — Campos numéricos, texto, email y formato de fecha
- ✅ **Confirmaciones** — Diálogos antes de eliminar o actualizar
- ✅ **Temas** — Modo Claro y Oscuro intercambiables en tiempo real
- ✅ **Favicon** — Ícono personalizado generado con Pillow

### Base de datos
- Motor: **SQLite**
- **Stored Procedures** implementados como Triggers:
  - `sp_insert_*`, `sp_update_*`, `sp_delete_*` para cada tabla
  - Tabla de **auditoría** automática que registra todas las operaciones

---

## 🗄️ Estructura de la base de datos

```sql
yacimientos  (codigo, nombre, ubicacion, mineral, metodo, fecha, reservas, vida, estado, imagen)
maquinaria   (serie, tipo, marca, modelo, capacidad, anio, horas, combustible, ubicacion, estado)
empleados    (id, nombre, cargo, edad, telefono, correo, direccion, fecha_ingreso, salario, imagen)
seguridad    (id, zona, riesgo, descripcion, fecha, responsable, accion, estado)
auditoria    (id, tabla, operacion, fecha, detalle)
```

---

## 🛠️ Tecnologías utilizadas

| Tecnología     | Uso                              |
|----------------|----------------------------------|
| Python 3        | Lenguaje principal               |
| Tkinter        | Interfaz gráfica                 |
| SQLite         | Base de datos                    |
| tkcalendar     | Selector de fechas               |
| Pillow         | Manejo de imágenes               |
| openpyxl       | Exportación a Excel              |
| reportlab      | Exportación a PDF                |

---

## 👨‍💻 Autor

**Andrés Muñoz**  
Proyecto académico — Sistema de Gestión Minera

---

## 📄 Licencia

Proyecto académico. Uso educativo.