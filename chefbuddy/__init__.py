from flask import Flask, render_template

from . import models
from .extensions import db, migrate, config, oauth, assets
from .views import chefbuddy, users


DATABASE_URI = "postgres://localhost/chefbuddy"
DEBUG = True
SECRET_KEY = 'development-key'
CONSUMER_KEY = '83d3feb6'
CONSUMER_SECRET = '9d5fcbd449d2f85767d52da8a2479246'


def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)

    app.register_blueprint(chefbuddy)
    app.register_blueprint(users)

    config.init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    return app
