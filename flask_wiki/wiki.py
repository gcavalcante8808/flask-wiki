from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask_wiki.backend import backend
from flask_wiki.frontend import frontend


debug = True
application = DispatcherMiddleware(frontend.app,
                                   {'/api': backend.app})

if debug:
    run_simple('0.0.0.0', 8000, application, use_reloader=True,
               use_debugger=True, use_evalex=True)
