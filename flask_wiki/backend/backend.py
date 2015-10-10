import os
from flask import Flask
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask_restful import Api
from flask_marshmallow import Marshmallow
from mixer.backend.flask import mixer
from flask_wiki.backend.models import db
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
# Use test_request_context is some kind of sorcery, but works?!
if app.config['BOOTSTRAP'] is True:
    with app.test_request_context():
        db.init_app(app)
        db.create_all()
else:
    db.init_app(app)

api = Api(app)
marsh = Marshmallow(app)
migrate = Migrate(app, db)
manager = Manager(app)
mixer.init_app(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
