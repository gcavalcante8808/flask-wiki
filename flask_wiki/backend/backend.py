import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask_restful import Api
from flask_marshmallow import Marshmallow

# TODO: Verify URL prefix implementation if debug is true.
# TODO: Verify Migrate Support.

PROJECT_ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
app.config['TESTING'] = True
app.config['BOOTSTRAP'] = True


app.config['DATABASE'] = 'wiki.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////%s/%s' % (PROJECT_ROOT_PATH,
                                                              app.config.get('DATABASE'))

# Database Configuration
if app.config['BOOTSTRAP'] is True:
    db = SQLAlchemy(app)
    db.create_all()
else:
    db = SQLAlchemy(app)

api = Api(app)
marsh = Marshmallow(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
