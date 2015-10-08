import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask_restful import Api
from src.backend.views import PageView


#TODO: Verify URL prefix implementation if debug is true.

PROJECT_ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
app.config['TESTING'] = True


app.config['DATABASE'] = 'wiki.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////%s/%s' % (PROJECT_ROOT_PATH,
                                                             app.config.get('DATABASE'))

api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if app.config['TESTING']:
    from src.backend.models import *
    db.create_all()
    migrate.init_app(app, db)

api.add_resource(PageView,'/pages-list', endpoint='pages_list')

if __name__ == '__main__':
    manager.run()
