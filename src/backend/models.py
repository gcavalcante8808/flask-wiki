from src.backend.backend import db


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    path = db.Column(db.String)
    raw_content = db.Column(db.Text)
    rendered_content = db.Column(db.Text)
    public = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return "<Page %s %s>" % (self.path, self.name)

    def __str__(self):
        return self.name
