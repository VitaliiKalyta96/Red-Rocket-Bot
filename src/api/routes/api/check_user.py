from flask import request
from src.api.app import app, db, api
from flask_restful import Resource
from src.api.models.models import User
from src.api.utils.helpers import convert_list, encrypt_string


class UsersResourse(Resource):
    def post(self):
        data = request.json
        user = User(username=data['username'],
                    email=data['email'],
                    password=encrypt_string(data['password']))
        db.session.add(user)
        db.session.commit()
        return user.serialize

    def get(self):
        users = User.query.all()
        return convert_list(users)


api.add_resource(UsersResourse, "/api/v1/users")