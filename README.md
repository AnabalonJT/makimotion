# MakiMotion - Sistema de Gestión de Pacientes

MakiMotion es un sistema web de gestión de pacientes diseñado para profesionales de la salud. Permite gestionar información de pacientes, programar citas y realizar seguimiento del progreso de los tratamientos.

## Características

- 🔐 **Autenticación de usuarios** - Sistema seguro de login/logout
- 👥 **Gestión de pacientes** - Crear, editar, ver y eliminar pacientes
- 📅 **Gestión de citas** - Programar y gestionar citas con evaluaciones de progreso
- 📊 **Dashboard intuitivo** - Vista general con estadísticas y ordenamiento
- 🎨 **Diseño responsivo** - Interfaz moderna con paleta de colores MakiMotion
- 🔒 **Aislamiento de datos** - Cada usuario solo ve sus propios pacientes

## Tecnologías Utilizadas

- **Backend**: Django 5.2.4
- **Base de datos**: SQLite (desarrollo) / PostgreSQL (producción)
- **Frontend**: HTML5, CSS3, JavaScript
- **Servidor web**: Gunicorn (producción)
- **Archivos estáticos**: WhiteNoise

## Instalación y Configuración

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Clonar el repositorio**
   ```bash
   git clone <repository-url>
   cd makimotion
   ```

2. **Crear un entorno virtual (recomendado)**
   ```bash
   python -m venv venv
   
   # En Windows
   venv\Scripts\activate
   
   # En macOS/Linux
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar migraciones**
   ```bash
   python manage.py migrate
   ```

5. **Crear un superusuario (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Iniciar el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

7. **Acceder a la aplicación**
   - Abrir navegador en: http://127.0.0.1:8000/
   - Panel de administración: http://127.0.0.1:8000/admin/

## Comandos Útiles

### Desarrollo
```bash
# Iniciar servidor de desarrollo
python manage.py runserver

# Crear migraciones después de cambios en modelos
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar tests
python manage.py test

# Recopilar archivos estáticos (para producción)
python manage.py collectstatic
```

### Producción
```bash
# Iniciar con Gunicorn
gunicorn makimotion.wsgi:application

# Con configuración específica
gunicorn makimotion.wsgi:application --bind 0.0.0.0:8000 --workers 3
```

## Estructura del Proyecto

```
makimotion/
├── core/                   # Aplicación principal
│   ├── models.py          # Modelos de datos (Patient, Appointment, UserProfile)
│   ├── views.py           # Vistas de la aplicación
│   ├── forms.py           # Formularios Django
│   ├── urls.py            # URLs de la aplicación
│   └── admin.py           # Configuración del admin
├── templates/             # Plantillas HTML
│   ├── base.html         # Plantilla base
│   ├── dashboard/        # Plantillas del dashboard
│   ├── patients/         # Plantillas de pacientes
│   └── auth/             # Plantillas de autenticación
├── static/               # Archivos estáticos
│   └── css/
│       └── style.css     # Estilos CSS principales
├── makimotion/           # Configuración del proyecto
│   ├── settings.py       # Configuración Django
│   ├── urls.py           # URLs principales
│   └── wsgi.py           # Configuración WSGI
├── manage.py             # Script de gestión Django
├── requirements.txt      # Dependencias Python
└── README.md            # Este archivo
```

## Configuración de Variables de Entorno

Para producción, configura las siguientes variables de entorno:

```bash
# Configuración de seguridad
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=False
ALLOWED_HOSTS=tu-dominio.com,www.tu-dominio.com

# Base de datos (opcional, usa SQLite por defecto)
DATABASE_URL=postgresql://usuario:password@host:puerto/database
```

## Paleta de Colores MakiMotion

La aplicación utiliza una paleta de colores suave y profesional:

- **Primary**: #d1a0f8 (Lila suave)
- **Secondary**: #f9c5d1 (Rosa suave)
- **Accent**: #ffffff (Blanco)
- **Neutral**: #f4effa (Fondo neutral)
- **Contrast**: #a86ef4 (Lila fuerte para botones)
- **Error**: #f87171 (Rojo suave para errores)

## Funcionalidades Principales

### Dashboard
- Vista general de todos los pacientes
- Estadísticas básicas
- Ordenamiento por nombre o fecha de última cita
- Acceso rápido a crear nuevo paciente

### Gestión de Pacientes
- **Crear**: Formulario con validación para nuevos pacientes
- **Ver**: Detalles completos del paciente e historial de citas
- **Editar**: Modificar información del paciente
- **Eliminar**: Eliminación con confirmación

### Gestión de Citas
- **Programar**: Nueva cita para un paciente específico
- **Evaluar**: Sistema de evaluación del progreso (Excelente, Bueno, Regular, etc.)
- **Historial**: Vista cronológica de todas las citas del paciente

## Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Soporte

Para reportar bugs o solicitar nuevas funcionalidades, por favor crea un issue en el repositorio del proyecto.

---

**MakiMotion** - Sistema de Gestión de Pacientes © 2025