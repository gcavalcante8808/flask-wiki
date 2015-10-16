from flask_wiki.backend.backend import marsh
from flask_wiki.backend.custom_serialization_fields import GUIDSerializationField
from flask_wiki.backend.models import Page
from marshmallow import fields

# TODO: Change it for ModelSchema.
class PageSchema(marsh.Schema):
    class Meta:
        model = Page

    guid = GUIDSerializationField()
    name = fields.String()
    raw_content = fields.String()
    rendered_content = fields.String()



page_schema = PageSchema()
pages_schema = PageSchema(many=True)
