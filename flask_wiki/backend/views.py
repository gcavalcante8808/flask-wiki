import markdown2
from flask_restful import Resource, reqparse, fields, marshal_with, marshal,\
    abort
from flask_wiki.backend.models import Page, db

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
page_parser.add_argument('raw_content', type=str, required=False)
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

    def post(self):
        # Get a a object and verify if exists;
        # if it does, return a 422 code and if not, create it.
        parser = reqparse.RequestParser()
        parser.add_argument('raw_content', type=str)
        parser.add_argument('name', type=str)
        parser.add_argument('rendered_content', type=str)
        args = parser.parse_args()

        # serializer = page_schema.dump(args)

        r = Page.query.filter_by(name=args.get('name')).first()
        if r:
            return marshal(r, page_fields), 422

        result = Page()
        result.raw_content = args.get('raw_content')
        result.name = args.get('name')
        result.rendered_content = render_markdown(result.raw_content)
        db.session.add(result)
        db.session.commit()

        return marshal(result, page_fields), 201

        # return serializer.errors, 400

    def put(self):
        # Stub for NotImplemented
        return 501

    def patch(self):
        # Stub for NotImplemented
        return 501


class PageDetail(Resource):
    def get(self, slug):
        """
        Return a specific object.
        :param slug:
        :return:
        """
        result = Page.query.filter_by(slug=slug).first()

        if not result:
            abort(404)

        return marshal(result, page_fields), 200

    def patch(self, slug):
        """
        Receive partial updates for an existing object.
        :param slug:
        :return:
        """
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


class MDRender(Resource):
    """
     Take a markdown text and render into HTML.
    """
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('raw_content', type=str)

        args = parser.parse_args()

        return render_markdown(args.get('raw_content'))
