# Project1: Wiki

## Description

This project is a Django-based web encyclopedia site called "wiki," which contains a single application called "encyclopedia."

### URL Configuration:
In `encyclopedia/urls.py`, the URL configuration for the application is defined. By default, there is a route associated with the `views.index` function.

### Utility Functions:
In `encyclopedia/util.py`, there are three key functions:
- `list_entries`: Returns a list of all the encyclopedia entry names.
- `save_entry`: Saves a new encyclopedia entry given a title and Markdown content.
- `get_entry`: Retrieves an entry by its title, returning its Markdown content or `None` if it doesn't exist.

These functions can be used in views to interact with encyclopedia entries, which are stored as Markdown files in the `entries/` directory.

### Initial View:
In `encyclopedia/views.py`, there is currently a single view, `index`, which returns a template `encyclopedia/index.html`. This view provides the template with a list of all the encyclopedia entries obtained via `util.list_entries`.

### Templates:
- The `encyclopedia/index.html` template is located in `encyclopedia/templates/encyclopedia/index.html`. It inherits from a base template `layout.html` and specifies the page title as well as the body content: an unordered list of all encyclopedia entries.
- `layout.html` defines the overall structure of the page, including a sidebar with a search field (which currently does nothing), a link to the home page, and links to create a new page or visit a random page (which don't work yet).

This structure provides the foundation for developing a dynamic and extensible web encyclopedia using Django.

Repository: [Project1: Wiki](https://github.com/sandovaldavid/project1_wiki.git)

## Features

- **Main Functionality**: Describes the project's main functionality.
- **Technologies Used**:
  - Python
  - Django
  - HTML/CSS
  - JavaScript

## Installation

Instructions for installing and running the project in a local environment:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/repository-name.git
2. ***Enter the project directory:***
    ```bash
    cd repository-name
3. ***Create a virtual environment:***
    ```bash
    python -m venv venv
4. ***Install dependencies:***
    ```bash
    pip install -r requirements.txt
5. ***Run the project:***
    ```bash
   python manage.py runserver

## Usage
Basic instructions on how to use the project once it's up and running:
1. Open your browser and visit http://127.0.0.1:8000/.
2. Interact with the available features as explained in the Features section.

## Project Structure
```
nombre-del-repositorio/
│
├── encyclopedia/       # Secondary Django application
├── entries/            # Markdown files of the encyclopedia entries
├── wiki/               # Main Django application
├── .gitignore          # Files and directories ignored by Git
├── manage.py           # Django management script
└── README.md           # Project documentation
└── requirements.txt    # Project dependencies
```
## Credits
Instructors: Brian Yu, David J. Malan
Course: CS50's Web Programming with Python and JavaScript

## Contact
For questions or suggestions, you can contact me by [email](mailto:sandovaldavid2201@gmail.com)