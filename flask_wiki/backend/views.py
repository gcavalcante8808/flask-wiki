from flask_restful import Resource, reqparse
from flask_wiki.backend.models import Page,db
from flask_wiki.backend.serializers import pages_schema, page_schema


class PageView(Resource):
    def get(self):
        pages = Page.query.all()
        result = pages_schema.dump(pages)
        return result.data

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('raw_content', type=str)
        parser.add_argument('name', type=str)
        args = parser.parse_args()

        serializer = page_schema.dump(args)

        if serializer.data and not serializer.errors:
            result = Page()
            result.raw_content = serializer.data.get('raw_content')
            result.name = serializer.data.get('name')

            print(result)
            db.session.add(result)
            db.session.commit()
            return {'data': serializer.data}, 201

        return serializer.errors, 400
