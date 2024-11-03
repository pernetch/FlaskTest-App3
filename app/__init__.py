
from flask import Flask, render_template, url_for, session, redirect, flash
from flask_bootstrap import Bootstrap5

from config import Config
from app.models import *
from app.forms import loginForm, addEventForm

bootstrap = Bootstrap5()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Config.init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

    
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = loginForm()
        return render_template('login.html', form = form)
    
    @app.route('/events')
    def events():
        events = Event.query.all()

        return render_template('events.html', events=events)
    
    @app.route('/add-event')
    def add_event():
        form = addEventForm()

        return render_template('add-event.html', form=form)

    @app.route('/user/<name>')
    def user_page(name):
        return render_template('user.html', name=name)

    return app
