from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_restful import Api
from src.backend.views import PageView

#TODO: Verify URL prefix implementation if debug is true.

app = Flask(__name__)
app.config['TESTING'] = True


app.config['DATABASE'] = 'wiki.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////%s' % app.config.get('DATABASE')
api = Api(app)
db = SQLAlchemy(app)


def init_db(db):
    # Create the db structure.
    db.create_all()

api.add_resource(PageView,'/pages-list', endpoint='pages_list')
