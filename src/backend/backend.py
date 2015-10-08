from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DATABASE'] = 'wiki.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////%s' % app.config.get('DATABASE')
db = SQLAlchemy(app)

def init_db(db):
    # Create the db structure.
    db.create_all()

