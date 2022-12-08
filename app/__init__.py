from flask import Flask
from flask_bootstrap import Bootstrap
from app.routes.ricky import bp_ricky
from app.config import Config
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Bootstrap(app)
    app.register_blueprint(bp_ricky)
    return app
