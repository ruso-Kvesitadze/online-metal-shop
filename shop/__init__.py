from flask import Flask
from shop.config import Config 
from shop.extensions import db , migrate, login_manager, mail
from shop.commands import init_db, populate_db
from shop.views.home.routes import home_blueprint
from shop.views.authentication.routes import authentication_blueprint
from shop.views.user_account.routes import user_account_blueprint
from shop.models import User

COMMANDS = [init_db, populate_db]
BLUEPRINTS = [home_blueprint,authentication_blueprint,user_account_blueprint]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_blueprint(app)
    register_extensions(app)
    register_commands(app)
    
    return app

def register_blueprint(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "authentication.login"

    @login_manager.user_loader
    def load_user(_id):
        return User.query.get(_id)
    
def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)