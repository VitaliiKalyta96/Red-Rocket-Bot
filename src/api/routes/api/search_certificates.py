from src.api.app import app, db, api
from flask_restful import Resource
from flask import request, jsonify, abort
from src.api.utils.helpers import convert_list
from src.api.models.models import Certificate


class CerticateSearch(Resource):
    def get(self):
        try:
            q = request.args.get('q')
            certificates = Certificate.query.filter_by(public_id=q).all()
            if not certificates:
                return jsonify({"status": False, "message": "Sorry,certificate with this id does not exist!"})
            if certificates:
                return convert_list(certificates)
        except Exception as ex:
            print(str(ex))
            abort(422)

class CerticateSearchOwner(Resource):
    def get(self):
        try:
            q = request.args.get('q')
            certificates = Certificate.query.filter_by(owner=q).all()
            if not certificates:
                return jsonify({"status": False, "message": "Sorry,owner does not exist!"})
            if certificates:
                return convert_list(certificates)
        except Exception as ex:
            print(str(ex))
            abort(422)

api.add_resource(CerticateSearch, "/api/v1/search")
api.add_resource(CerticateSearchOwner, "/api/v1/search/owner")
