from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate


app = Flask(__name__)
api = Api(app)
db = SQLAlchemy()
app.config.from_object("config.Config")
db.init_app(app)
migrate = Migrate(app, db)
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json"]
app.config["JWT_COOKIE_SECURE"] = False
jwt_manager = JWTManager()

with app.app_context():
    from routes.api import *
    from routes.main import *
    from auth import *
    from models import User, Event, Category, Certificate


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=7070)
