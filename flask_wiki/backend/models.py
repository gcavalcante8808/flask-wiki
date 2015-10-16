import uuid
from flask.ext.sqlalchemy import SQLAlchemy
from flask_wiki.backend.custom_fields import GUIDField

db = SQLAlchemy()


#TODO: Add Owner and other security fields later.
class Page(db.Model):
    """
    Implements the Page Model.
    """
    guid = db.Column(GUIDField, primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String, nullable=False)
    raw_content = db.Column(db.Text)
    rendered_content = db.Column(db.Text)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name
