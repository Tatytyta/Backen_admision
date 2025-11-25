# API de Admisión - Backend Django REST Framework

Sistema de gestión de admisiones universitarias desarrollado con Django REST Framework y PostgreSQL con autenticación JWT y sistema de permisos.

## Requisitos Previos

- Python 3.13 o superior
- PostgreSQL 12 o superior
- pip (gestor de paquetes de Python)
- pgAdmin (opcional, para gestionar la base de datos)

## Instalación y Ejecución del Backend

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd admision_api
```

### 2. Crear y activar el entorno virtual

Windows:
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Linux/Mac:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crear un archivo .env en la raíz del proyecto:

```env
SECRET_KEY=super-secret-key
DEBUG=True
ALLOWED_HOSTS=10.0.2.2

DB_NAME=admision
DB_USER=postgres
DB_PASS=admin
DB_HOST=localhost
DB_PORT=5432

JWT_ACCESS_MINUTES=60
JWT_REFRESH_DAYS=7
```

### 5. Crear la base de datos PostgreSQL

Abrir pgAdmin o la terminal de PostgreSQL y ejecutar:

```sql
CREATE DATABASE admision;
```

### 6. Aplicar migraciones

```bash
python manage.py migrate
```

### 7. Crear usuarios de prueba

```bash
python manage.py crear_usuarios_prueba
```

Esto crea:
- Administrador: admin / admin123
- Usuario Normal: user / user123

### 8. Ejecutar el servidor

```bash
python manage.py runserver
```

El servidor estará disponible en: http://127.0.0.1:8000

## Sistema de Permisos

La API implementa dos roles de usuario:

Usuario Normal (is_staff=False)
- Puede consultar (GET) todos los recursos
- Puede crear, actualizar y eliminar: Institutos, Carreras, Solicitudes, Resultados
- NO puede modificar Estudiantes (solo lectura)

Administrador (is_staff=True)
- Acceso completo a todas las operaciones CRUD
- Puede crear otros administradores
- Sin restricciones

## Ejemplos de Uso de la API

### 1. Login y obtener token

POST {{base_url}}/api/auth/login/
Content-Type: application/json

```json
{
  "username": "admin",
  "password": "admin"
}
```

Respuesta:
```json
{
    "message": "Login exitoso",
    "user": {
        "id": 1,
        "username": "admin",
        "email": "admin@gmail.com",
        "first_name": "",
        "last_name": "",
        "is_admin": true,
        "is_staff": true,
        "is_superuser": true
    },
    "tokens": {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2NDYzOTA5NCwiaWF0IjoxNzY0MDM0Mjk0LCJqdGkiOiJjZDZmNzdhYTlkNTk0ZTUxOTkxNDk0OTljOWNkODI1MCIsInVzZXJfaWQiOiIxIn0.dZMkF2QV6uT_XMMGrBkplc8JhCnpkYeaY0AMRotTnFE",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY0MDM3ODk0LCJpYXQiOjE3NjQwMzQyOTQsImp0aSI6Ijc0NjZhN2YzYzczMjQ2YjI5MDE1MmU4ZTEzNmUzMTczIiwidXNlcl9pZCI6IjEifQ.ibbvBNNm2ExYjoF-nuPngsO11K_ggpyTxYc4BOkY5DI"
    }
}
```

### 2. Consultar tu perfil

{{base_url}}/api/auth/profile/
Authorization: Bearer {access_token}

### 3. Crear un Instituto

POST {{base_url}}/api/institutos/
Authorization: Bearer {access_token}
Content-Type: application/json

```json
{
  "nombre": "Instituto Tecnológico Superior",
  "direccion": "Av. Principal 123",
  "telefono": "555-0123",
  "email": "contacto@its.edu"
}
```

### 4. Crear una Carrera

POST {{base_url}}/api/carreras/
Authorization: Bearer {access_token}
Content-Type: application/json

```json
{
    "nombre": "Ingeniería en Sistemas",
    "duracion_anios": 5,
    "instituto": 1
}
```

### 5. Crear un Estudiante (Solo Admin)

POST {{base_url}}/api/estudiantes/
Authorization: Bearer {access_token}
Content-Type: application/json

```json
{
  "nombre": "Juan",
  "apellido": "Pérez",
  "fecha_nacimiento": "2000-05-15",
  "email": "juan.perez@email.com",
  "telefono": "555-9876",
  "direccion": "Calle Falsa 456",
  "documento_identidad": "12345678"
}
```

### 6. Crear una Solicitud

POST {{base_url}}/api/solicitudes/
Authorization: Bearer {access_token}
Content-Type: application/json

```json
{
  "fecha_solicitud": "2025-11-24",
  "estado": "Pendiente",
  "estudiante": 1,
  "carrera": 1
}
```

### 7. Actualizar Parcialmente una Solicitud

PATCH {{base_url}}/api/solicitudes/2/
Authorization: Bearer {access_token}
Content-Type: application/json

```json
{
    "estado": "Rechazado"
}
```

### 8. Crear un Resultado

POST {{base_url}}/api/resultados/
Authorization: Bearer {access_token}
Content-Type: application/json

```json
{
    "solicitud": 2,
    "fecha_resultado": "2025-11-25",
    "resultado": "Aprobado",
    "observaciones": "Cumple con todos los requisitos"
}
```

### 9. Listar con Paginación

GET {{base_url}}/api/institutos/
Authorization: Bearer {access_token}

### 10. Eliminar un Recurso

DELETE {{base_url}}/api/carreras/1/
Authorization: Bearer {access_token}

## Listado de Endpoints

Base URL: {{base_url}}

### Autenticación (Sin token requerido)

POST /api/auth/login/ - Iniciar sesión
POST /api/auth/register/ - Registrar nuevo usuario

### Autenticación (Con token)

POST /api/auth/logout/ - Cerrar sesión
GET /api/auth/profile/ - Ver perfil actual

### Institutos (Token requerido - CRUD completo)

GET /api/institutos/ - Listar todos
POST /api/institutos/ - Crear nuevo
GET /api/institutos/{id}/ - Ver detalle
PUT /api/institutos/{id}/ - Actualizar completo
PATCH /api/institutos/{id}/ - Actualizar parcial
DELETE /api/institutos/{id}/ - Eliminar

### Carreras (Token requerido - CRUD completo)

GET /api/carreras/ - Listar todas
POST /api/carreras/ - Crear nueva
GET /api/carreras/{id}/ - Ver detalle
PUT /api/carreras/{id}/ - Actualizar completa
PATCH /api/carreras/{id}/ - Actualizar parcial
DELETE /api/carreras/{id}/ - Eliminar

### Estudiantes (Token requerido - Solo Admin puede modificar)

GET /api/estudiantes/ - Listar todos
POST /api/estudiantes/ - Crear nuevo (Solo Admin)
GET /api/estudiantes/{id}/ - Ver detalle
PUT /api/estudiantes/{id}/ - Actualizar completo (Solo Admin)
PATCH /api/estudiantes/{id}/ - Actualizar parcial (Solo Admin)
DELETE /api/estudiantes/{id}/ - Eliminar (Solo Admin)

### Solicitudes (Token requerido - CRUD completo)

GET /api/solicitudes/ - Listar todas
POST /api/solicitudes/ - Crear nueva
GET /api/solicitudes/{id}/ - Ver detalle
PUT /api/solicitudes/{id}/ - Actualizar completa
PATCH /api/solicitudes/{id}/ - Actualizar parcial
DELETE /api/solicitudes/{id}/ - Eliminar

### Resultados (Token requerido - CRUD completo)

GET /api/resultados/ - Listar todos
POST /api/resultados/ - Crear nuevo
GET /api/resultados/{id}/ - Ver detalle
PUT /api/resultados/{id}/ - Actualizar completo
PATCH /api/resultados/{id}/ - Actualizar parcial
DELETE /api/resultados/{id}/ - Eliminar

## Colección de Postman

Se incluye el archivo Admision_API_Actualizada.postman_collection.json en la raíz del proyecto.

### Cómo importar en Postman:

1. Abrir Postman
2. Click en Import
3. Seleccionar el archivo Admision_API_Actualizada.postman_collection.json
4. Click en Import

### Características de la colección:

- Todos los endpoints organizados por carpetas
- Script automático que guarda el token después del login
- Variables de entorno preconfiguradas
- Ejemplos de peticiones para todos los métodos CRUD

### Cómo usar la colección:

1. Ejecutar Login - Usuario Normal o Login - Administrador
2. El token se guardará automáticamente
3. Todos los demás endpoints usarán el token guardado
4. Listo para probar todos los endpoints

## Estructura del Proyecto

```
admision_api/
├── admision_api/
│   ├── settings.py              # Configuración de Django
│   ├── urls.py                  # URLs principales
│   └── core/
│       ├── models/              # Modelos de datos
│       │   ├── estudiante.py
│       │   ├── instituto.py
│       │   ├── carrera.py
│       │   ├── solicitud.py
│       │   └── resultado.py
│       ├── serializers/         # Serializers de DRF
│       │   ├── auth.py
│       │   ├── estudiante.py
│       │   ├── instituto.py
│       │   ├── carrera.py
│       │   ├── solicitud.py
│       │   └── resultado.py
│       ├── views/               # ViewSets de la API
│       │   ├── auth.py
│       │   ├── estudiante.py
│       │   ├── instituto.py
│       │   ├── carrera.py
│       │   ├── solicitud.py
│       │   └── resultado.py
│       ├── permissions.py       # Permisos personalizados
│       ├── urls.py              # URLs de la API
│       └── management/
│           └── commands/
│               └── crear_usuarios_prueba.py
├── manage.py
├── requirements.txt
├── README.md
├── PERMISOS.md
├── PRUEBAS_PERMISOS.md
├── Admision_API_Actualizada.postman_collection.json
└── .env
```

## Modelos de Datos

### Estudiante
- nombre: CharField
- apellido: CharField
- fecha_nacimiento: DateField
- email: CharField
- telefono: CharField
- direccion: CharField
- documento_identidad: CharField (único)

### Instituto
- nombre: CharField
- direccion: CharField
- telefono: CharField
- email: CharField

### Carrera
- nombre: CharField
- duracion_anios: IntegerField
- instituto: ForeignKey a Instituto

### Solicitud
- fecha_solicitud: DateField
- estado: CharField
- estudiante: ForeignKey a Estudiante
- carrera: ForeignKey a Carrera

### Resultado
- solicitud: OneToOneField a Solicitud
- fecha_resultado: DateField
- resultado: CharField
- observaciones: CharField

## Tecnologías Utilizadas

- Django 5.2.8 - Framework web
- Django REST Framework 3.16.1 - API REST
- PostgreSQL - Base de datos
- djangorestframework-simplejwt 5.5.1 - Autenticación JWT
- django-filter 25.2 - Filtrado de datos
- psycopg2-binary 2.9.11 - Adaptador PostgreSQL
- python-dotenv 1.2.1 - Variables de entorno

## Configuración Adicional

### Paginación

La API está configurada con paginación automática:
- Tamaño de página: 10 registros
- Parámetro: ?page=número

### Filtrado y Búsqueda

La API soporta filtrado, búsqueda y ordenamiento mediante Django Filter.

### Panel de Administración

Acceder al panel de administración en: http://127.0.0.1:8000/admin/

## Solución de Problemas

### Error: No module named django

Asegurarse de tener el entorno virtual activado:

Windows:
```powershell
.venv\Scripts\Activate.ps1
```

Linux/Mac:
```bash
source .venv/bin/activate
```

### Error de conexión a PostgreSQL

- Verificar que PostgreSQL esté corriendo
- Verificar credenciales en el archivo .env
- Verificar que la base de datos admision exista

### Error de migraciones

```bash
python manage.py migrate
```
