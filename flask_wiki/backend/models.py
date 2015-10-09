from sqlalchemy import UniqueConstraint
from flask.ext.sqlalchemy import SQLAlchemy
from flask_wiki.backend.custom_fields import GUIDField

db = SQLAlchemy()


#TODO: Add Owner and other security fields later.
class Page(db.Model):
    guid = db.Column(GUIDField, primary_key=True)
    name = db.Column(db.String)
    path = db.Column(db.String)
    raw_content = db.Column(db.Text)
    rendered_content = db.Column(db.Text)

    UniqueConstraint('name','path')

    def __repr__(self):
        return "<Page %s %s>" % (self.path, self.name)

    def __str__(self):
        return self.name
