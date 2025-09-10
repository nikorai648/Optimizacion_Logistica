 #  Optimizacion y Logística

Sistema de gestión desarrollado en **Django** para administrar **Trabajadores, Asistencias y Accidentes** en una empresa de construcción.  
Incluye autenticación de usuarios, CRUD completo para cada entidad y un diseño responsivo con **Bootstrap + CSS personalizado**.

---

##  Características principales
-  **Login y Logout** de usuarios (con protección de vistas usando `@login_required`).
-  **Gestión de trabajadores** (alta, edición, baja, listado).
-  **Control de asistencias** con horas extra, atrasos y estados (presente, ausente, licencia, vacaciones).
-  **Registro de accidentes** con detalle de gravedad, lugar, licencia y trabajadores involucrados.
-  **Interfaz con Bootstrap 5** + estilos personalizados en `estilos.css`.
-   Soporte de imágenes e íconos para cada sección.
-   Navegación centralizada mediante menú superior.

---

##  Estructura del proyecto:
Optimizacion_Logistica/
│
├── core/ # App principal
│ ├── migrations/
│ ├── templates/
│ │ └── core/ # Templates de cada entidad
│ │ ├── home.html
│ │ ├── trabajador_list.html
│ │ ├── asistencia_list.html
│ │ └── accidente_list.html
│ ├── static/
│ │ ├── css/estilos.css
│ │ └── img/ # Logos e íconos
│ ├── admin.py
│ ├── forms.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
│
├── Optimizacion_Logistica/ # Configuración global
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── db.sqlite3 # Base de datos (SQLite)
└── manage.py


---

##  Instalación y configuración

### 1. Clonar repositorio
```bash
git clone https://github.com/nikorai648/Optimizacion_Logistica.git
cd optimizacion-logistica

Crear entorno virtual
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

Instalar dependencias
pip install -r requirements.txt

Migrar base de datos
python manage.py makemigrations
python manage.py migrate

Crear superusuario
python manage.py createsuperuser

Levantar servidor de desarrollo
python manage.py runserver

Autenticación

Acceder al login en: /accounts/login/

Logout implementado vía formulario POST en la barra de navegación.

Solo usuarios autenticados pueden acceder a CRUD de trabajadores, asistencias y accidentes.

 Estilos e imágenes

Bootstrap 5.3.3 cargado vía CDN.

Estilos personalizados en static/css/estilos.css.

Fondo beige aplicado solo al contenido principal (<main>).

Logos e íconos en static/img/.

Funcionalidades CRUD
Trabajador

Crear, editar, eliminar, listar.

Atributos: rut, nombre, apellido, cargo, contrato, turno, sueldo, etc.

Asistencia

Relación 1:N con trabajador.

Atributos: fecha, hora entrada, hora salida, atraso, horas extra, estado, observaciones.

Accidente

Relación N:N con trabajadores.

Atributos: fecha, tipo, gravedad, lugar, licencia, días de licencia, costo, observaciones.

 Requisitos técnicos

Python 3.10+ (probado en 3.13)

Django 5.2.5

Bootstrap 5.3.3

Base de datos: SQLite (por defecto)
