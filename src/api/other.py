from flask import Flask
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app)


events = [
    {
        "id": 1,
        "name_mentor": "Kelly",
        "data_time": "10-12-2021"
    },
    {
        "id": 2,
        "mentor": "Jack",
        "data_time": "17-12-2021"
    }
]


class Quote(Resource):
    def get(self, id=0):
        if id == 0:
            return events, 200
        for quote in events:
            if(quote["id"] == id):
                return quote, 200
        return "Quote not found", 404

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("name_mentor")
        parser.add_argument("data_time")
        params = parser.parse_args()
        for event in events:
            if (id == event["id"]):
                return f"Quote with id {id} already exists", 400
        event = {
            "id": id,
            "name_mentor": params["name_mentor"],
            "data_time": params["data_time"]
        }

        events.append(event)
        return event, 201

    def delete(self, id):
        global events
        events = [event for event in events if event["id"] != id]
        return f"Event with id {id} is deleted.", 201


api.add_resource(Quote, "/api/events", "/api/events/<int:id>")

if __name__=="__main__":
    app.run(debug=True)