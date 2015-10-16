import uuid
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from flask_wiki.backend.custom_fields import GUIDField

db = SQLAlchemy()


#TODO: Add Owner and other security fields later.
class Page(db.Model):
    """
    Implements the Page Model.
    """
    guid = db.Column(GUIDField, primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String, nullable=False, unique=True)
    raw_content = db.Column(db.Text, nullable=False, unique=True)
    rendered_content = db.Column(db.Text)

    UniqueConstraint('name', 'raw_content')

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name
