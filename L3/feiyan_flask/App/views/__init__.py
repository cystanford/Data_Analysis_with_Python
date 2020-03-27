
from App.views.api import api


def init_blue(app):
    app.register_blueprint(blueprint=api)