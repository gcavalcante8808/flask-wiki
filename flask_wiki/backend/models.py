from sqlalchemy import UniqueConstraint
from flask.ext.sqlalchemy import SQLAlchemy
from flask_wiki.backend.custom_fields import GUIDField

db = SQLAlchemy()


#TODO: Add Owner and other security fields later.
class Page(db.Model):
    """
    Implements the Page Model. This model will use nested sets
    to define objects position in the tree, through
    left and right methods (named lft and rgt because of SQL99
    name restrictions)
    """
    guid = db.Column(GUIDField, primary_key=True)
    name = db.Column(db.String)
    lft = db.Column(db.Integer)
    rgt = db.Column(db.Integer)
    raw_content = db.Column(db.Text)
    rendered_content = db.Column(db.Text)

    UniqueConstraint('lft','rgt')

    def __repr__(self):
        return "<Page %s %s>" % (self.path, self.name)

    def __str__(self):
        return self.name
