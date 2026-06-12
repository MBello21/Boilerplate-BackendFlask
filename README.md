
Readme · MD
# 🚀 Flask API Boilerplate
 
Una estructura base limpia, moderna y lista para producción para construir APIs REST con **Python y Flask**. Incluye entorno de desarrollo completamente containerizado con VS Code Dev Containers y configuración de despliegue lista para servidor.
 
![Python](https://img.shields.io/badge/python-3.14-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask-3.0-white?style=for-the-badge&logo=flask&logoColor=black)
![PostgreSQL](https://img.shields.io/badge/postgresql-17-4169e1?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Pipenv](https://img.shields.io/badge/pipenv-latest-6b578c?style=for-the-badge&logo=python&logoColor=white)
 
---
 
## ✨ Características
 
- **Dev Container listo** — abre el proyecto en VS Code y el entorno se configura solo
- **PostgreSQL 17** incluido via Docker Compose
- **Migraciones automáticas** con Flask-Migrate y Alembic
- **Estructura desacoplada** — backend completamente independiente del frontend
- **Configuración de producción** incluida con `docker-compose.prod.yml`
- **PgAdmin** incluido en el stack de producción
- **Variables de entorno** gestionadas con `.env` y `.env.example`
---
 
## 🛠️ Stack
 
| Tecnología | Uso |
|---|---|
| Python 3.14 | Lenguaje base |
| Flask 3.x | Framework web |
| Flask-SQLAlchemy | ORM |
| Flask-Migrate | Migraciones de base de datos |
| PostgreSQL 17 | Base de datos |
| Pipenv | Gestión de dependencias y entorno virtual |
| Docker + Docker Compose | Containerización dev y producción |
| VS Code Dev Containers | Entorno de desarrollo reproducible |
 
---
 
## 📁 Estructura del proyecto
 
```
├── .devcontainer/
│   ├── devcontainer.json         # Configuración del Dev Container
│   ├── docker-compose.yml        # Stack de desarrollo
│   ├── docker-compose.prod.yml   # Stack de producción
│   ├── DockerFile                # Imagen base de desarrollo
│   └── Dockerfile.prod           # Imagen optimizada para producción
├── migrations/                   # Migraciones de base de datos (Alembic)
├── src/
│   └── api/
│       ├── models.py             # Modelos de base de datos
│       ├── routes.py             # Endpoints de la API
│       └── init.py               # Inicialización de la app
│   └── app.py                    # Punto de entrada
├── .env.example                  # Plantilla de variables de entorno
├── Pipfile                       # Dependencias del proyecto
└── Pipfile.lock                  # Versiones exactas de dependencias
```
 
---
 
## ⚙️ Inicio rápido — Desarrollo con Dev Container
 
> **Requisitos:** VS Code + extensión [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) + Docker Desktop
 
1. **Clona el repositorio:**
```bash
   git clone https://github.com/tu_usuario/tu_repo.git
   cd tu_repo
```
 
2. **Crea el archivo de variables de entorno del Dev Container:**
```bash
   cp .env.example .devcontainer/.env
```
   Edita `.devcontainer/.env` con tus valores:
```
   POSTGRES_USER=tu_usuario
   POSTGRES_PASSWORD=tu_password
   POSTGRES_DB=tu_base_de_datos
   DATABASE_URL=postgresql://tu_usuario:tu_password@localhost:5432/tu_base_de_datos
   FLASK_APP=src/app.py
```
 
3. **Abre VS Code y selecciona "Reopen in Container"**
   El entorno se configura automáticamente:
   - Instala todas las dependencias via `pipenv install`
   - Levanta PostgreSQL
   - Aplica las migraciones
4. **¡Listo!** La API está disponible en `http://localhost:5000/api`
---
 
## 🗃️ Gestión de la base de datos
 
```bash
# Generar nueva migración tras cambiar los modelos
pipenv run flask db migrate -m "descripcion del cambio"
 
# Aplicar migraciones pendientes
pipenv run flask db upgrade
 
# Revertir la última migración
pipenv run flask db downgrade
```
 
---
 
## 🌐 Endpoints de ejemplo
 
| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/api/health` | Estado de la API |
 
> Añade tus propios endpoints en `src/api/routes.py`
 
---
 
## 🚢 Despliegue en producción
 
El boilerplate incluye configuración lista para desplegar en cualquier servidor con Docker.
 
### Variables de entorno necesarias en producción
 
Crea un archivo `.env` en la raíz del servidor con:
 
```
POSTGRES_USER=tu_usuario
POSTGRES_PASSWORD=tu_password_seguro
POSTGRES_DB=tu_base_de_datos
FLASK_APP=src/app.py
DATABASE_URL=postgresql://tu_usuario:tu_password@db:5432/tu_base_de_datos
PGADMIN_DEFAULT_EMAIL=tu@email.com
PGADMIN_DEFAULT_PASSWORD=tu_password_pgadmin
```
 
> ⚠️ En producción la `DATABASE_URL` usa `db` como host (nombre del servicio Docker), no `localhost`.
 
### Levantar en producción
 
```bash
# Desde la raíz del proyecto en el servidor
docker compose -f .devcontainer/docker-compose.prod.yml up -d --build
```
 
Las migraciones se aplican automáticamente al arrancar.
 
### Servicios expuestos
 
| Servicio | Puerto | Descripción |
|---|---|---|
| Flask API | 5000 | API REST |
| PostgreSQL | 5432 | Base de datos |
| PgAdmin | 5050 | Gestor visual de BD |
 
---
 
## 🔐 Seguridad
 
- El archivo `.env` está en `.gitignore` — **nunca lo subas al repositorio**
- Usa `.env.example` como plantilla pública sin valores reales
- En producción gestiona las variables directamente en el servidor o usa un vault
---
 
## 📄 Licencia
 
MIT — libre para usar, modificar y distribuir.