# OnlyFlans

## Descripción

Este proyecto está diseñado para gestionar una aplicación web utilizando Django y PostgreSQL. Está estructurado de manera que cada funcionalidad o hito se desarrolla en ramas separadas para facilitar el seguimiento y ser usado como punto de control.

## Estructura de Ramas

El proyecto utiliza un sistema de control de versiones con ramas en Git para organizar el desarrollo. Cada hito o funcionalidad solicitada se implementa en ramas específicas. A continuación se detalla la estructura de ramas:

- **main**: Rama principal que contiene la versión actual del proyecto.
- **hito-1**: Rama dedicada al primer hito solicitado (Levantando tu primer proyecto Django).


## Instalación

Para configurar el proyecto en tu máquina local, sigue estos pasos:

1. Clona el repositorio:

   ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio

2. Crea y activa un entorno virtual:

   ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`

3. Instala las dependencias:

   ```bash
    pip install -r requirements.txt

4. Clona el repositorio:

    - Asegúrate de que PostgreSQL esté instalado y en funcionamiento.
    - Crea una base de datos para el proyecto.
    - Configura las credenciales en settings.py.


5. Aplica las migraciones:

   ```bash
    python manage.py migrate


6. Ejecuta el servidor:

   ```bash
    python manage.py runserver
