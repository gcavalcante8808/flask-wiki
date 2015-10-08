from flask_wiki.backend.backend import marsh
from marshmallow import fields


class PageSchema(marsh.Schema):
    name = fields.String()
    path = fields.String()
    raw_content = fields.String()
    rendered_content = fields.String()


page_schema = PageSchema()
pages_schema = PageSchema(many=True)
