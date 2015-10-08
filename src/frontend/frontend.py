from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

frontend = Blueprint(__file__, __name__,
                    template_folder='templates')


@frontend.route('/', defaults={'page': 'index'})
@frontend.route('/<page>')
def show(page):
    """
    Try to Delive a page or abort with a 404 error.
    :param page: name of the page
    :return: template.
    """
    try:
        return render_template('pages/%s.html' % page)
    except (TemplateNotFound,):
        abort(404)