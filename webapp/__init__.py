from flask import Flask
from webapp.settings import enviroment
from webapp.swagger_docs.config import template, swagger_config
from flasgger import Swagger

swagger = Swagger(config=swagger_config, template=template)


def create_app():
    app = Flask(__name__)

    # instantiate swagger extension
    swagger.init_app(app, )

    # setting up the enviromnent
    if enviroment == 'development':
        app.config.from_object('webapp.settings.Config')
    else:
        app.config.from_object('webapp.settings.ProductionConfig')

    # importing the sorting route
    from .api.route import sorting

    # register the sorting route
    app.register_blueprint(sorting)

    return app
