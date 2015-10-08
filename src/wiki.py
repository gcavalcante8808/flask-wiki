import os
from flask import Flask, Blueprint, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from src.backend.backend import backend
from src.frontend.frontend import frontend

PROJECT_ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
app.register_blueprint(backend)
app.register_blueprint(frontend)
app.debug = True

app.config['DATABASE'] = 'wiki.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////%s' % app.config.get('DATABASE')

db = SQLAlchemy(app)


def init_db(db):
    # Create the db structure.
    db.create_all()

if __name__ == '__main__':
    app.run()