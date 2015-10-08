from flask import Blueprint

backend = Blueprint(__file__, __name__,
                    template_folder='templates')
