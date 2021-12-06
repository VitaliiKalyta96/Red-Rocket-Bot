from flask import request
from flask_restful import Resource

from app import app, api, db
from models import Event
from utils.helpers import convert_list


class EventResourse(Resource):
    def get(self):
        events = Event.query.all()
        return convert_list(events)

    def post(self):
        data = request.json
        event = Event(name_mentor=data['name_mentor'], date=data['date'], time=data['time'])
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
        event.name_mentor = data['name_mentor'] if data.get('name_mentor', False) else event.name_mentor
        event.date = data['date'] if data.get('date', False) else event.date
        event.time = data['time'] if data.get('time', False) else event.time
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