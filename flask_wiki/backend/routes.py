from flask_wiki.backend.backend import api
from flask_wiki.backend.views import PageView

api.add_resource(PageView, '/pages-list', endpoint='pages-list')