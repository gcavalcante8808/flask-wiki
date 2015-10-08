from flask_restful import Resource, Api

class HomeView(Resource):
    def get(self, page_id):
        return {'page_id': page_id}

    def post(self, page_id):
        return {'page_id': page_id}