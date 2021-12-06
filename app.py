from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy()
app.config.from_object("config.Config")
db.init_app(app)
migrate = Migrate(app, db)


with app.app_context():
    from routes.api import *
    from routes.main import *
    from models import Event

    db.create_all()


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=7070)