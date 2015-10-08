from flask_restful import Resource
from src.backend.models import Page
from src.backend.serializers import pages_schema


class PageView(Resource):
    def get(self):
        pages = Page.query.all()
        result = pages_schema.dump(pages)
        return result.data
