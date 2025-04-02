# Project1: Wiki 📚

![GitHub](https://img.shields.io/github/license/sandovaldavid/project-01-wiki)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Django](https://img.shields.io/badge/Django-5.1-green)
![Markdown](https://img.shields.io/badge/Markdown-5B5B5B)

A Wikipedia-like web encyclopedia built as part of Harvard's CS50's Web Programming with Python and JavaScript course.

*Read this in [Spanish](README_es.md) | [English](README_en.md)*

## 🚀 Overview

This Django-based encyclopedia allows users to:
- 📄 View encyclopedia entries rendered from Markdown to HTML
- 🔍 Search for entries with partial matching suggestions
- ✏️ Create new entries using Markdown syntax
- 📝 Edit existing entries
- 🎲 Navigate to random entries

## 💻 Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript
- **Content Format**: Markdown
- **Development Tools**: Git, Virtual Environment

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sandovaldavid/project-01-wiki.git
   ```

2. **Set up the environment:**
   ```bash
   cd project-01-wiki
   python -m venv venv
   source venv/bin/activate    # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python manage.py runserver
   ```

4. **Access the website at** `http://127.0.0.1:8000/`

## 🔍 Project Structure

```
project1_wiki/
│
├── encyclopedia/       # Django app containing views, templates and utilities
├── entries/            # Markdown files of encyclopedia entries
├── wiki/               # Main Django project configuration
├── .gitignore          # Git ignore specifications
├── manage.py           # Django command-line utility
└── requirements.txt    # Python dependencies
```

## 🎓 About This Project

This project is part of **Harvard's CS50 Web Programming with Python and JavaScript** course. It implements a Wikipedia-like encyclopedia using Django, focusing on:
- Server-side rendering with Django templates
- Content manipulation using Python
- Markdown-to-HTML conversion
- Form handling and validation
- URL routing and request handling

## 👨‍💻 Credits

- **Instructors**: Brian Yu, David J. Malan
- **Course**: [CS50's Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/)
- **Developer**: [David Sandoval](https://github.com/sandovaldavid)

## 📬 Contact

For questions or suggestions, contact me via [email](mailto:xdevs@devprojects.tech)

