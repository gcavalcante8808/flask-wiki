from flask_wiki.backend.backend import api
from flask_wiki.backend.views import PageView, PageDetail, MDRender

api.add_resource(PageView, '/pages-list', endpoint='pages-list')
api.add_resource(PageDetail, '/pages/<slug>', endpoint='page-detail')
api.add_resource(MDRender, '/md-render', endpoint='md-render')
