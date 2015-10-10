import uuid
from sqlalchemy import UniqueConstraint, CheckConstraint, Index
from sqlalchemy.sql.expression import text
from sqlalchemy import event
from flask.ext.sqlalchemy import SQLAlchemy
from flask_wiki.backend.custom_fields import GUIDField

db = SQLAlchemy(session_options={'expire_on_commit': False})


#TODO: Add Owner and other security fields later.
class Page(db.Model):
    """
    Implements the Page Model. This model will use nested sets
    to define objects position in the tree, through
    left and right methods (named lft and rgt because of SQL99
    name restrictions)
    """
    guid = db.Column(GUIDField, primary_key=True, default=uuid.uuid4())
    name = db.Column(db.String, nullable=False)
    lft = db.Column(db.Integer, nullable=False)
    rgt = db.Column(db.Integer)
    raw_content = db.Column(db.Text)
    rendered_content = db.Column(db.Text)

    # UniqueTogether lft and rgt
    UniqueConstraint('lft', 'rgt')

    # Lft value should be inferior to rgt value.
    CheckConstraint('lft < rgt', name='valid_range_pair')

    # The RGT value should be gt 1
    CheckConstraint('rgt > 1', name='valid_rgt')

    # Minimal value for lft is 1 (root Node)
    CheckConstraint('lft > 0', name='valid_lft')

    # Weight should not be negative
    CheckConstraint('wgt >= 0', name='non_negative_wgt')

    # Quantity should not be negative
    CheckConstraint('qty > 0', name='positive_qty')

    # Index for lft and rgt
    Index('idx_lft_rgt', 'lft', 'rgt', unique=True)

    def __repr__(self):
        return "<Page %s,%s %s>" % (self.lft, self.rgt, self.name)

    def __str__(self):
        return self.name

    @property
    def root(self):
        # Return the root of the tree
        result = self.query.filter_by(lft=1).all()
        return result

    @property
    def leafs(self):
        # Return list of Leafs (Nodes without Children)
        result = self.query.filter(text('lft = (rgt - 1)')).all()
        return result


@event.listens_for(Page, 'before_insert')
def page_defaults(mapper, configuration, target):
    # If no RGT is provided, one will be generated using lft column.
    if not target.rgt:
        target.rgt = target.lft + 1

@event.listens_for(Page, 'before_insert')
@event.listens_for(Page, 'before_delete')
def update_root_rgt(mapper, configuration, target):
    # Time to update the RGT of root object.
    new_rgt = Page.query.count() * 2
    target.query.filter_by(lft=1).update(values={'rgt':new_rgt})
