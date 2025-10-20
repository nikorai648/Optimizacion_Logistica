 #  Optimizacion y Logística

Sistema de gestión desarrollado en Django 5.2.5 para administrar Trabajadores, Asistencias, Accidentes, Desempeños, Eficiencias y Sueldos dentro de una empresa de construcción.
El sistema permite el control integral de personal con autenticación, CRUD completo y una interfaz moderna con Bootstrap 5 + CSS personalizado.

---

Características principales

Autenticación segura de usuarios

Login y logout implementados con protección de rutas (@login_required).

Solo usuarios autenticados pueden acceder al sistema.

CRUD completos para todas las entidades:

Trabajador → Registro de datos personales, laborales y de contacto.

Asistencia → Control diario con hora de entrada/salida, atrasos, horas extra y estado.

Accidente → Registro detallado de incidentes, gravedad, costos y observaciones.

Eficiencia del trabajador → Seguimiento de productividad mensual.

Desempeño del trabajador → Evaluación cualitativa sobre forma de trabajo y quejas.

Sueldo del trabajador → Cálculo del sueldo mensual según cantidad y tipo de trabajos realizados.

Diseño responsivo y visual

Interfaz con Bootstrap 5.3.3 y colores personalizados.

Iconos e imágenes representativos en cada módulo (/static/img).

Navegación intuitiva

Menú principal con accesos a todas las secciones.

Botones de acción claros para agregar, editar o eliminar registros.

Validaciones integradas

Modelos y formularios con validaciones de tipo, longitud y rango (validators, choices).

Migración de base de datos

Proyecto capaz de ser migrado, usando MySQL Workbench y credenciales configuradas en settings.py.


Optimizacion_Logistica/
│
├── core/                         # Aplicación principal
│   ├── migrations/               # Archivos de migración de Django
│   ├── templates/core/           # Templates de cada módulo
│   │   ├── home.html
│   │   ├── trabajador_*.html
│   │   ├── asistencia_*.html
│   │   ├── accidente_*.html
│   │   ├── desempeno_*.html
│   │   ├── eficiencia_*.html
│   │   └── sueldo_*.html
│   ├── static/                   # Recursos estáticos (CSS / imágenes)
│   │   ├── css/estilos.css
│   │   └── img/
│   ├── admin.py                  # Configuración del panel administrativo
│   ├── forms.py                  # Formularios de cada modelo
│   ├── models.py                 # Definición de tablas y validaciones
│   ├── urls.py                   # Rutas específicas de la app
│   └── views.py                  # Lógica CRUD (List, Create, Update, Delete)
│
├── Optimizacion_Logistica/       # Configuración global del proyecto
│   ├── settings.py               # Configuración general (MySQL, templates, static, etc.)
│   ├── urls.py                   # Enrutamiento general
│   └── wsgi.py                   # Despliegue
│
├── manage.py                     # Herramienta de ejecución y migraciones
└── requirements.txt              # Dependencias del entorno


---

##  Instalación y configuración

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

En Optimizacion_Logistica/settings.py ya se encuentra configurado el acceso a MySQL:

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


💡 En MySQL Workbench debe existir la base de datos optimizacion_logistica y el usuario django_user.

5. Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

6. Crear usuario administrador
python manage.py createsuperuser

7. Iniciar el servidor
python manage.py runserver


Luego accede a:

Panel admin: http://127.0.0.1:8000/admin/

Aplicación principal: http://127.0.0.1:8000/

🧑‍💻 Módulos del sistema
Módulo	Descripción	Principales campos
Trabajador	Gestión de datos personales y laborales.	rut, nombre, cargo, turno, estado
Asistencia	Registro diario de asistencia y horas extra.	fecha, estado, hora_entrada, hora_salida
Accidente	Detalle de incidentes y gravedad.	fecha, tipo, gravedad, lugar, dias_licencia
Desempeño	Evaluación de la forma de trabajo del empleado.	trabajador_rut, forma_de_hacer_trabajos, posibles_quejas
Eficiencia	Registra cantidad de trabajos completados y sueldos promedio.	trabajos_completados_en_1_mes, sueldo_promedio_informado
Sueldo	Nuevo módulo agregado: relaciona sueldo con tipo y cantidad de trabajos del mes.	mes, cantidad_trabajos_mes, tipo_trabajos_mes, sueldo_total_mes
🎨 Interfaz y estética

Herencia de templates usando {% extends 'base.html' %}.

Protección CSRF en formularios mediante {% csrf_token %}.

Imágenes organizadas en static/img/ (trabajador, asistencia, accidente, etc.).

Diseño adaptado: fondo claro, botones diferenciados por color y tipografía limpia.

🧩 Requisitos técnicos

Python 3.13+

Django 5.2.5

MySQL 8.0+

Bootstrap 5.3.3