import uuid
import markdown2
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint, event
from flask_wiki.backend.custom_fields import GUIDField
from slugify import slugify

db = SQLAlchemy()


# TODO: Add Owner and other security fields later.
class Page(db.Model):
    """
    Implements the Page Model.
    """
    guid = db.Column(GUIDField, primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String, nullable=False, unique=True)
    raw_content = db.Column(db.Text, nullable=False, unique=True)
    rendered_content = db.Column(db.Text)
    slug = db.Column(db.String, nullable=False, unique=True)

    UniqueConstraint('name', 'raw_content')

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name


def make_slug(mapper, connection, target):
    target.slug = slugify(target.name)


def render_html(mapper, connection, target):
    target.rendered_content = markdown2.markdown(target.raw_content)

event.listen(Page, 'before_insert', make_slug)
event.listen(Page, 'before_insert', render_html)
