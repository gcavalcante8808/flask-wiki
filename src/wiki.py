from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

app.config['DATABASE'] = 'wiki.db'
app.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite:////%s' % app.config.get('DATABASE')
db = SQLAlchemy(app)


def init_db(db):
    db.create_all()

if __name__ == '__main__':
    app.run()