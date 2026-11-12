# E-Market
## Project Overview
A Django product-catalog application with relational product data, image uploads, filtering, and server-rendered pages. This is a development project, not a complete checkout or payment platform.

## Problem Statement
Keep product, category, supplier, price, and stock information together and make a small catalog searchable through a web interface.

## Key Features
- List products and view individual details.
- Add products through a ModelForm with optional image uploads.
- Delete products after a confirmation page and POST request.
- Filter by maximum price, category name, and supplier name.
- Search categories and suppliers and display related product counts.
- Bootstrap-styled forms and Django CSRF middleware.

## Technologies Used
Python, Django 5.2.9 (recorded in the settings header), SQLite, HTML, CSS, Bootstrap 5, and Pillow for image fields. Dependency versions are not currently locked.

## Architecture Overview
Django URL routes call function-based views. Views use ModelForms and the ORM, then render templates. Products reference categories and suppliers through foreign keys. Uploaded files use a local media directory.

## Project Structure
| Path | Responsibility |
| --- | --- |
| `emarket/models.py` | Product, Category, and Supplier models |
| `emarket/views.py` | Catalog operations and search |
| `emarket/forms.py` | Product ModelForm |
| `emarket/urls.py` | Application routes |
| `labExam/` | Django configuration |
| `templates/` | Server-rendered pages |
| `static/` | Styles and product assets |

## Installation
Use Python 3.10 or newer. From the repository root:
```sh
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell alternative:
# .venv\Scripts\Activate.ps1
python -m pip install "Django==5.2.9" Pillow
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
These are source-derived setup instructions; a clean installation has not been verified as part of the documentation update.

## Configuration
The checked-in settings use SQLite, local media storage, DEBUG mode, a development-only secret, and permissive hosts. Before any deployment, supply a new private secret, disable debug, restrict hosts, and review authentication and authorization on catalog writes. Do not reuse the checked-in key.

Django's admin endpoint exists, but the application models are not registered in `emarket/admin.py`. Create local Category and Supplier records through the Django shell before adding a product:
```sh
python manage.py shell
```
```python
from emarket.models import Category, Supplier
Category.objects.get_or_create(catName="General")
Supplier.objects.get_or_create(suppName="Local supplier", Location="Local")
```

## Usage
Open `http://127.0.0.1:8000/`. Browse `/products/`, add at `/products/add/`, and search at `/search/`. The application has no cart, payment integration, or REST API.

## Future Improvements
- Lock dependencies and add a repeatable clean-install check.
- Add authorization for write operations and register catalog models in admin.
- Add validation for non-negative prices and quantities, pagination, and focused tests.
- Move deployment configuration into environment variables and document production media storage.

## Author
[Albarq-CS](https://github.com/Albarq-CS)
