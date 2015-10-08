import os
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

PROJECT_ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
app.debug = True

app.config['DATABASE'] = 'wiki.db'
app.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite:////%s' % app.config.get('DATABASE')
db = SQLAlchemy(app)


@app.route('/')
def root():
    # Index Page
    return render_template('index.html')

def init_db(db):
    # Create the db structure.
    db.create_all()

if __name__ == '__main__':
    app.run()