from flask_wiki.backend.backend import marsh
from flask_wiki.backend.custom_serialization_fields import GUIDSerializationField
from marshmallow import fields


class PageSchema(marsh.Schema):
    guid = GUIDSerializationField()
    name = fields.String()
    path = fields.String()
    raw_content = fields.String()
    rendered_content = fields.String()


page_schema = PageSchema()
pages_schema = PageSchema(many=True)
