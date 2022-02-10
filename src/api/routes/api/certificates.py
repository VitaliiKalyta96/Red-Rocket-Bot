from flask import request
from flask_restful import Resource

from src.api.app import app, api, db
from src.api.models.models import Certificate
from src.api.utils.helpers import convert_list


class CertificateResourse(Resource):
    def get(self):
        certificates = Certificate.query.all()
        return convert_list(certificates)

    def post(self):
        data = request.json
        certificates = Certificate(title=data['title'], description=data['description'],
                     owner=data['owner'], mentor=data['mentor'],  date=data['date'])
        db.session.add(certificates)
        db.session.commit()
        return certificates.serialize


class CertificateResourseID(Resource):

    def get(self, id):
        try:
            certificates = Certificate.query.get(id)
            return certificates.serialize
        except Exception:
            return f"ERROR: Certificate with the ID {id} not found", 404

    def put(self, id):
        data = request.json
        certificates = Certificate.query.get(id)
        certificates.title = data['title'] if data.get('title', False) else certificates.title
        certificates.description = data['description'] if data.get('description', False) else certificates.description
        certificates.owner = data['owner'] if data.get('owner', False) else certificates.owmer
        certificates.mentor = data['mentor'] if data.get('mentor', False) else certificates.mentor
        certificates.date = data['date'] if data.get('date', False) else certificates.date_time
        db.session.add(certificates)
        db.session.commit()
        return certificates.serialize

    def delete(self, id):
        try:
            certificates = Certificate.query.get(id)
            db.session.delete(certificates)
            db.session.commit()
            return f"WARNING: Certificate with the ID {id} was destroyed", 204
        except Exception:
            return f"ERROR: Certificate with the ID {id} not found", 404


api.add_resource(CertificateResourse, "/api/v1/certificates")
api.add_resource(CertificateResourseID, "/api/v1/certificates/<int:id>")
