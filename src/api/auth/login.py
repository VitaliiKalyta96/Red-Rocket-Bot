import datetime
import jwt
from flask import request, jsonify, make_response
# from flask_jwt_extended import JWTManager
# from flask_jwt_extended import jwt_required, unset_jwt_cookies

from src.api.app import app
from src.api.config import Config
from src.api.models import User
from src.api.utils.helpers import encrypt_string, token_required


# jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    response = {
        "success": False,
        "message": "Invalid parameters",
        "token": ""
    }
    try:
        form = request.form

        user = User.query.filter(User.email == form['email']).filter(
            User.password == encrypt_string(form['password'])).first()
        print(user)

        # return make_response('Could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})

        if not user:
            response["message"] = "Unauthorized Access!"
            return response, 401

        if user:
            token = jwt.encode(
                {'id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=14)},
                Config.SECRET_KEY)
            response["message"] = "token generated"
            response["token"] = token.decode('UTF-8')
            response["success"] = True
            return response, 200
    except Exception as ex:
        print(str(ex))
        return response, 422

#will work on this
# @app.route('/logout')
# def logout():
#     @jwt_required
#     def delete(self):
#         # return response and reset access token
#         response = jsonify({"status": True, "message": "logout successful"})
#         unset_jwt_cookies(response)
#         return make_response(response, 200)