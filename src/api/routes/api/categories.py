from flask import request
from flask_restful import Resource

from app import app, api, db
from models.models import Category
from utils.helpers import convert_list


class CategoryResourse(Resource):
    def get(self):
        categories = Category.query.all()
        return convert_list(categories)

    def post(self):
        data = request.json
        category = Category(title=data['title'], description=data['description'])
        db.session.add(category)
        db.session.commit()
        return category.serialize


class CategoryResourseID(Resource):

    def get(self, id):
        category = Category.query.get(id)
        return category.serialize

    def put(self, id):
        data = request.json
        category = Category.query.get(id)
        category.title = data['title'] if data.get('title', False) else category.title
        category.description = data['description'] if data.get('description', False) else category.description
        db.session.add(category)
        db.session.commit()
        return category.serialize

    def delete(self, id):
        category = Category.query.get(id)
        db.session.delete(category)
        db.session.commit()
        return "Category with id {id} is deleted.", 204


api.add_resource(CategoryResourse, "/api/v1/events/categories")
api.add_resource(CategoryResourseID, "/api/v1/events/categories/<int:id>")