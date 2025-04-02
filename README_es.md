# Proyecto1: Wiki 📚

![GitHub](https://img.shields.io/github/license/sandovaldavid/project-01-wiki)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Django](https://img.shields.io/badge/Django-5.1-green)
![Markdown](https://img.shields.io/badge/Markdown-5B5B5B)

Una enciclopedia web al estilo de Wikipedia construida como parte del curso CS50's Web Programming with Python and JavaScript de Harvard.

*Leer esto en [Español](README_es.md) | [English](README.md)*

## 🚀 Descripción General

Esta enciclopedia basada en Django permite a los usuarios:
- 📄 Ver entradas de la enciclopedia renderizadas desde Markdown a HTML
- 🔍 Buscar entradas con sugerencias de coincidencia parcial
- ✏️ Crear nuevas entradas utilizando sintaxis Markdown
- 📝 Editar entradas existentes
- 🎲 Navegar a entradas aleatorias

## 💻 Tecnologías Utilizadas

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript
- **Formato de Contenido**: Markdown
- **Herramientas de Desarrollo**: Git, Entorno Virtual

## 📦 Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/sandovaldavid/project-01-wiki.git
   ```

2. **Configurar el entorno:**
   ```bash
   cd project-01-wiki
   python -m venv venv
   source venv/bin/activate    # En Windows usar: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación:**
   ```bash
   python manage.py runserver
   ```

4. **Acceder al sitio web en** `http://127.0.0.1:8000/`

## 🔍 Estructura del Proyecto

```
project1_wiki/
│
├── encyclopedia/       # Aplicación de Django con vistas, plantillas y utilidades
├── entries/            # Archivos Markdown de las entradas de la enciclopedia
├── wiki/               # Configuración principal del proyecto Django
├── .gitignore          # Especificaciones de archivos ignorados por Git
├── manage.py           # Utilidad de línea de comandos de Django
└── requirements.txt    # Dependencias de Python
```

## 🎓 Acerca de Este Proyecto

Este proyecto es parte del curso **Harvard's CS50 Web Programming with Python and JavaScript**. Implementa una enciclopedia similar a Wikipedia utilizando Django, enfocándose en:
- Renderizado del lado del servidor con plantillas de Django
- Manipulación de contenido usando Python
- Conversión de Markdown a HTML
- Manejo y validación de formularios
- Enrutamiento de URL y manejo de solicitudes

## 👨‍💻 Créditos

- **Profesores**: Brian Yu, David J. Malan
- **Curso**: [CS50's Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/)
- **Desarrollador**: [David Sandoval](https://github.com/sandovaldavid)

## 📬 Contacto

Para preguntas o sugerencias, contáctame por [correo electrónico](mailto:xdevs@devprojects.tech)