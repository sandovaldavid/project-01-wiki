# Proyecto1: Wiki

## Descripción

Este proyecto es un sitio web tipo enciclopedia construido con Django, llamado "wiki", que contiene una única aplicación llamada "encyclopedia".

### Configuración de URL:
En ``encyclopedia/urls.py``, se define la configuración de URL de la aplicación. Por defecto, existe una ruta que está asociada a la función ``views.index``.

### Funciones de Utilidad:
En ``encyclopedia/util.py``, se encuentran tres funciones clave:
- ``list_entries``: Devuelve una lista con los nombres de todas las entradas de la enciclopedia.
- ``save_entry``: Guarda una nueva entrada en la enciclopedia, dado un título y contenido en Markdown.
- ``get_entry``: Recupera una entrada por su título, devolviendo su contenido en Markdown o None si no existe.

Estas funciones pueden ser utilizadas en las vistas para interactuar con las entradas de la enciclopedia, las cuales se almacenan como archivos Markdown en el directorio ``entries/``.

### Vista Inicial:
En ``encyclopedia/views.py``, actualmente existe una única vista, index, que devuelve una plantilla ``encyclopedia/index.html``. Esta vista proporciona a la plantilla una lista de todas las entradas de la enciclopedia obtenida a través de ``util.list_entries``.
### Plantillas:
- La plantilla ``encyclopedia/index.html`` se encuentra en ``encyclopedia/templates/encyclopedia/index.html``. Hereda de una plantilla base ``layout.html`` y especifica el título de la página, así como el contenido del cuerpo de la página: una lista desordenada de todas las entradas de la enciclopedia.
- ``layout.html`` define la estructura general de la página, incluyendo una barra lateral con un campo de búsqueda (que actualmente no funciona), un enlace a la página principal, y enlaces para crear una nueva página o visitar una página aleatoria (que aún no funcionan).

Este esquema proporciona la base para desarrollar una enciclopedia web dinámica y extensible utilizando Django.

Repository: [Project1: Wiki](https://github.com/sandovaldavid/project1_wiki.git)

## Características

- **Funcionalidad Principal**: Describe la funcionalidad principal del proyecto.
- **Tecnologías Utilizadas**:
  - Python
  - Django
  - HTML/CSS
  - JavaScript

## Instalación

Instrucciones para instalar y ejecutar el proyecto en un entorno local:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tuusuario/nombre-del-repositorio.git
2. ***Entrar al directorio del proyecto:***
    ```bash
    cd nombre-del-repositorio
3. ***Crear un entorno virtual:***
    ```bash
    python -m venv venv
4. ***Instalar las dependencias:***
    ```bash
    pip install -r requirements.txt
5. ***Ejecutar el proyecto:***
    ```bash
   python manage.py runserver
## Uso
Instrucciones básicas sobre cómo utilizar el proyecto una vez que esté en funcionamiento.
1. Abre tu navegador y visita http://127.0.0.1:8000/.
2. Interactúa con las funcionalidades disponibles según lo explicado en la sección de características.

## Estructura del proyecto
```
nombre-del-repositorio/
│
├── encyclopedia/       # aplicacion secundaria de Django
├── entries/            # Archivos Markdown de las entradas de la enciclopedia
├── wiki/               # Aplicacion principal de Django
├── .gitignore          # Archivos y directorios ignorados por Git
├── manage.py           # Script de gestión de Django
└── README.md           # Documentación del proyecto
└── requirements.txt    # Dependencias del proyecto
```
## Créditos
Profesores: Brian Yu, David J. Malan
Curso: CS50's Web Programming with Python and JavaScript

## Contacto
Para preguntas o sugerencias, puedes contactar a través de del siguiente [correo electrónico](mailto:sandovaldavid2201@gmail.com)