import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask_restful import Api
from flask_marshmallow import Marshmallow


# TODO: Verify URL prefix implementation if debug is true.
# TODO: Verify Migrate Support.

PROJECT_ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
app.config['TESTING'] = True
app.config['BOOTSTRAP'] = False


app.config['DATABASE'] = 'wiki.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////%s/%s' % (PROJECT_ROOT_PATH,
                                                              app.config.get('DATABASE'))

api = Api(app)
manager = Manager(app)
marsh = Marshmallow(app)


# Database Configuration
if app.config['BOOTSTRAP'] is True:
    from src.backend.models import *
    db = SQLAlchemy(app, session_options={
        'expire_on_commit': False
    })
    db.create_all()
else:
    db = SQLAlchemy(app)

# Routing Configuration.
# TODO: Avoiding Circular imports in this way is UGLY. Verify.
from src.backend.views import PageView
api.add_resource(PageView,'/pages-list', endpoint='pages_list')

if __name__ == '__main__':
    manager.run()
