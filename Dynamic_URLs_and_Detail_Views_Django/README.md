# Dynamic URLs and Detail Views in Django

## Description
This project demonstrates how to create dynamic URL patterns in Django that capture parameters directly from the URL to display detailed information. The focus is on building URLs that accept variables (e.g., student IDs) and using these to fetch and render specific data in views and templates.

Key features include:
- Defining URL patterns with parameters in `urls.py`.
- Generating dynamic links in templates using Django's `{% url %}` tag.
- Implementing view functions that accept URL parameters and retrieve corresponding model instances.
- Rendering detailed data in templates based on the URL parameters.
- Connecting the home page's student cards to their respective detailed views.

## Technologies
- Python 3
- Django
- Bootstrap (for styling)

## How to Run
1. Make sure Python 3 and Django are installed.
2. Run the Django development server:

```bash
python manage.py runserver

