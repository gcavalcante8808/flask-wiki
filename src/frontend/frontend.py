from flask import Flask, render_template, abort
from jinja2 import TemplateNotFound

app = Flask(__name__)


@app.route('/', defaults={'page': 'index'})
def show(page):
    """
    Try to Deliver the default page.
    :param page: name of the page
    :return: template.
    """
    try:
        return render_template('pages/%s.html' % page)
    except (TemplateNotFound,):
        abort(404)