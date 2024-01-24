# {{cookiecutter.project_name}}

This is a simple Flask project that creates `/` route and renders an index.html page

## Getting Started

### Prerequisites

- Python 3.x
- [Virtualenv](https://virtualenv.pypa.io/)


# Project Structure
```
{{cookiecutter.project_name}}/
├── README.md
├── app
│   ├── __init__.py
│   └── templates
│       └── home.html
├── config.py
├── requirements.txt
└── run.py

```
# How to Run
## Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Install dependencies:
```
pip install -r requirements.txt
```

## Run the Flask app:
```
(venv) ➜  python3 run.py
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 933-952-624
```
The app will be accessible at http://127.0.0.1:5000/
---
This README provides a basic overview of the project structure, components, and instructions on how to run and test the Flask app. Customize it further based on your project's specific details and requirements.

