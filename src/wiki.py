from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
from src.backend import backend
from src.frontend import frontend


debug = True
application = DispatcherMiddleware(frontend.app,
                                   {'/api': backend.app})

if debug:
    run_simple('localhost', 8000, application, use_reloader=True,
               use_debugger=True, use_evalex=True)