from flask_restful import Resource


class PageView(Resource):
    def get(self):
        return {'hello':'world'}
