from flask import Flask, render_template, abort, redirect, url_for
from flask.ext.script import Manager
from jinja2 import TemplateNotFound

app = Flask(__name__)
app.config['TESTING'] = True
manager = Manager(app)


@app.route('/', endpoint='frontend-index')
def root():
    # Redirect Base URL for the real Index Page.
    return redirect(url_for('frontend-pages', page='index'))


@app.route('/<page>', endpoint='frontend-pages')
def show(page='index'):
    """
    Try to Deliver a page.
    :param page: name of the page
    :return: template.
    """
    try:
        return render_template('pages/index.html')
    except (TemplateNotFound,):
        abort(404)

if __name__ == '__main__':
    manager.run()
