from flask_restful import Resource, reqparse
from flask_wiki.backend.models import Page,db
from flask_wiki.backend.serializers import pages_schema, page_schema


class PageView(Resource):
    def get(self):
        # Just Dump all Pages for now.
        pages = Page.query.all()
        result = pages_schema.dump(pages)
        return result.data

    def post(self):
        # Get a a object and verify if exists; if it does, return a 422 code and if not, create it.
        parser = reqparse.RequestParser()
        parser.add_argument('raw_content', type=str)
        parser.add_argument('name', type=str)
        args = parser.parse_args()

        serializer = page_schema.dump(args)

        if serializer.data and not serializer.errors:
            r = Page.query.filter_by(name=serializer.data.get('name', None)).first()
            if r:
                return {'data': serializer.data,
                        'message': "The object already exist. Use PATCH to update the object."}, 422

            result = Page()
            result.raw_content = serializer.data.get('raw_content')
            result.name = serializer.data.get('name')

            db.session.add(result)
            db.session.commit()
            return {'data': serializer.data}, 201

        return serializer.errors, 400

    def put(self):
        # Stub for NotImplemented
        return 501

    def patch(self):
        # Stub for NotImplemented
        return 501


class PageDetail(Resource):
    def get(self, slug):
        result = Page.query.filter_by(slug=slug).first()
        if not result:
            return 404

        serializer = page_schema.dump(result)
        return {'data': serializer.data}, 200
