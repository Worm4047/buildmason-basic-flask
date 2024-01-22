# app/__init__.py

from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('home.html')

    # Add more routes and configurations as needed

    return app
