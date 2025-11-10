 #  Optimizacion y Logística

Optimizacion y Logística

Sistema de gestión desarrollado en Django 5.2.5 para administrar Trabajadores, Asistencias, Accidentes, Desempeños, Eficiencias y Sueldos dentro de una empresa de construcción.
El sistema implementa un modelo de datos relacional, con autenticación de usuarios, operaciones CRUD completas y una interfaz moderna desarrollada con Bootstrap 5 y CSS personalizado.

Características principales
Autenticación segura de usuarios

Login y logout implementados con protección de rutas (@login_required).

Solo los usuarios autenticados pueden acceder al sistema.

CRUD completos con relaciones entre tablas

El proyecto fue mejorado incorporando relaciones reales entre las entidades, asegurando integridad referencial y consistencia de datos.

Entidad	Relación	Descripción
TipoTrabajador	1 → N	Define el cargo y tipo de contrato de un conjunto de trabajadores.
Trabajador	N → 1 con TipoTrabajador	Cada trabajador pertenece a un tipo definido (por ejemplo, “Obrero - Plazo Fijo”).
Asistencia	N → 1 con Trabajador	Cada registro de asistencia está asociado a un trabajador específico.
Accidente	N ↔ N con Trabajador	Un accidente puede involucrar a varios trabajadores y viceversa.
EficienciaTrabajador	N → 1 con Trabajador	Registra la eficiencia mensual de un trabajador.
DesempenoTrabajador	N → 1 con Trabajador	Evalúa el desempeño individual del trabajador.
SueldoTrabajador	N → 1 con Trabajador y 1 → N con EficienciaTrabajador	Calcula el sueldo mensual considerando su eficiencia.
Diseño responsivo y visual

Interfaz moderna construida con Bootstrap 5.3.3.

Uso de imágenes representativas en cada módulo (/static/img).

Fondo personalizable y estilo uniforme en todo el sistema.

Herencia de templates con {% extends 'base.html' %} y uso de {% block content %}.

Formularios protegidos con tokens CSRF ({% csrf_token %}).

Validaciones integradas

Validaciones en modelos (validators, choices, unique=True).

Validaciones en formularios (ModelForm con reglas de tipo y formato).

Campos numéricos y de texto limitados a rangos válidos.

Migración de base de datos

El proyecto fue migrado exitosamente a MySQL, utilizando credenciales configuradas en settings.py.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'optimizacion_logistica',
        'USER': 'django_user',
        'PASSWORD': '6487063a1234',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


💡 Se debe crear la base de datos optimizacion_logistica y el usuario django_user con los permisos adecuados.

Estructura del proyecto
Optimizacion_Logistica/
│
├── core/                         # Aplicación principal
│   ├── migrations/               # Migraciones de base de datos
│   ├── templates/core/           # Templates de cada módulo
│   │   ├── home.html
│   │   ├── trabajador_*.html
│   │   ├── asistencia_*.html
│   │   ├── accidente_*.html
│   │   ├── desempeno_*.html
│   │   ├── eficiencia_*.html
│   │   └── sueldo_*.html
│   ├── static/                   # Archivos estáticos
│   │   ├── css/estilos.css
│   │   └── img/
│   ├── admin.py                  # Configuración del panel de administración
│   ├── forms.py                  # Formularios de cada entidad
│   ├── models.py                 # Definición de tablas y relaciones
│   ├── urls.py                   # Enrutamiento interno de la app
│   └── views.py                  # Lógica CRUD (List, Create, Update, Delete)
│
├── Optimizacion_Logistica/       # Configuración global del proyecto
│   ├── settings.py               # Configuración general (MySQL, static, templates)
│   ├── urls.py                   # Enrutamiento general
│   └── wsgi.py                   # Despliegue
│
├── manage.py                     # Comando principal del proyecto
└── requirements.txt              # Dependencias del entorno

Instalación y configuración
1. Clonar el repositorio
git clone https://github.com/nikorai648/Optimizacion_Logistica.git
cd Optimizacion_Logistica

2. Crear entorno virtual
python -m venv venv
venv\Scripts\activate  # Windows
# o
source venv/bin/activate  # Linux/Mac

3. Instalar dependencias
pip install -r requirements.txt

4. Configurar base de datos MySQL

Asegúrate de tener MySQL corriendo y con el usuario django_user creado.

5. Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

6. Crear usuario administrador
python manage.py createsuperuser

7. Iniciar el servidor
python manage.py runserver

Acceso al sistema

Panel de administración: http://127.0.0.1:8000/admin/

Aplicación principal: http://127.0.0.1:8000/

Módulos del sistema
Módulo	Descripción	Principales campos
Trabajador	Gestión de datos personales y laborales.	rut, nombre, tipo (FK TipoTrabajador), turno, estado.
Asistencia	Registro diario de asistencia.	trabajador (FK), fecha, hora_entrada, hora_salida, estado.
Accidente	Detalle de incidentes y gravedad.	fecha, tipo, gravedad, lugar, trabajadores (ManyToMany).
Desempeño	Evaluación del desempeño del trabajador.	trabajador (FK), forma_de_hacer_trabajos, posibles_quejas.
Eficiencia	Registra productividad mensual.	trabajador (FK), trabajos_completados_en_1_mes, sueldo_promedio_informado.
Sueldo	Relaciona el sueldo con la eficiencia mensual.	trabajador (FK), mes, cantidad_trabajos_mes, eficiencia (FK).
Interfaz y estética

Plantillas heredadas desde base.html.

Protección CSRF en todos los formularios.

Imágenes en /static/img/ y estilos en /static/css/estilos.css.

Diseño claro, moderno y adaptado a dispositivos móviles.

Requisitos técnicos

Python 3.13+

Django 5.2.5

MySQL 8.0+

Bootstrap 5.3.3