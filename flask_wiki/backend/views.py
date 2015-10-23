import markdown2
from flask import abort
from flask_restful import Resource, reqparse, fields, marshal_with, marshal
from flask_wiki.backend.models import Page, db
from flask_wiki.backend.serializers import page_schema

page_fields = {
    'guid': fields.String,
    'name': fields.String,
    'raw_content': fields.String,
    'rendered_content': fields.String,
    'slug': fields.String
}

page_parser = reqparse.RequestParser()
page_parser.add_argument('guid', type=str, required=False)
page_parser.add_argument('name', type=str, required=False)
page_parser.add_argument('raw_content', type=str,required=False)
page_parser.add_argument('rendered_content', type=str, required=False)
page_parser.add_argument('slug', type=str, required=False)


def render_markdown(text):
    """
    Take a markdown text and render into HTML.
    :param text:
    :return:
    """
    return markdown2.markdown(text)


class PageView(Resource):
    @marshal_with(page_fields)
    def get(self):
        # Just Dump all Pages for now.
        pages = Page.query.all()
        return pages

    # TODO: Migrate post format to marshal.
    def post(self):
        # Get a a object and verify if exists; if it does, return a 422 code and if not, create it.
        parser = reqparse.RequestParser()
        parser.add_argument('raw_content', type=str)
        parser.add_argument('name', type=str)
        parser.add_argument('rendered_content', type=str)
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
            result.rendered_content = render_markdown(result.raw_content)
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
    @marshal_with(page_fields)
    def get(self, slug):
        result = Page.query.filter_by(slug=slug).first()
        if not result:
            abort(404, message="Page {} doesn't exist.".format(slug))
        return result

    def patch(self, slug):
        result = Page.query.filter_by(slug=slug).first()
        if not result:
            return 404

        args = page_parser.parse_args()

        for key, value in args.items():
            if value is not None:
                setattr(result, key, value)

        db.session.add(result)
        db.session.commit()

        return marshal(result, page_fields), 204
