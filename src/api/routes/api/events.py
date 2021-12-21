from flask import request
from flask_restful import Resource

from app import app, api, db
from models.models import Event
from utils.helpers import convert_list


class EventResourse(Resource):
    def get(self):
        events = Event.query.all()
        return convert_list(events)

    def post(self):
        data = request.json
        event = Event(title=data['title'], description=data['description'],
                      date_time=data['date_time'], category=data['category'], link=data['link'])
        db.session.add(event)
        db.session.commit()
        return event.serialize


class EventResourseID(Resource):

    def get(self, id):
        event = Event.query.get(id)
        return event.serialize

    def put(self, id):
        data = request.json
        event = Event.query.get(id)
        event.title = data['title'] if data.get('title', False) else event.title
        event.description = data['description'] if data.get('description', False) else event.description
        event.date_time = data['date_time'] if data.get('date_time', False) else event.date_time
        event.category = data['category'] if data.get('category', False) else event.category
        event.link = data['link'] if data.get('link', False) else event.link
        db.session.add(event)
        db.session.commit()
        return event.serialize

    def delete(self, id):
        event = Event.query.get(id)
        db.session.delete(event)
        db.session.commit()
        return "Event with id {id} is deleted.", 204


api.add_resource(EventResourse, "/api/v1/events")
api.add_resource(EventResourseID, "/api/v1/events/<int:id>")