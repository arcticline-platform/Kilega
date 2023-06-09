from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from .utils import db
from .auth.view import auth_namespace
from .config.config import config_dict
from .config.config import enviroment

def create_app():
    app=Flask(__name__)

    # app.config.from_object(config)
    if  enviroment == "production":
        app.config.from_object(config_dict['production'])
    else:
        app.config.from_object(config_dict['development'])

    authorizations={
        "Bearer Auth":{
            'type':"apiKey",
            'in':'header',
            'name':"Authorization",
            'description':"Add a JWT with ** Bearer &lt;JWT&gt; to authorize"
        }
    }
    api=Api(app,
        title="Kilega API",
        description="A REST API for Anglican Order Service",
        authorizations=authorizations,
        security="Bearer Auth"
    )

    api.add_namespace(auth_namespace, path='/auth')

    db.init_app(app)
    
    # all cross origin resource sharing 
    CORS(app)

    migrate=Migrate(app, db)

    jwt=JWTManager(app)

    # @app.shell_context_processor
    # def make_shell_context():
    #     return {
    #         'db': db,
    #         'User': User
    #     }

    return app
