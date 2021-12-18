from flask import request

from src.api.app import app, db
from src.api.models.models import User
from src.api.utils.helpers  import encrypt_string, check_email, checking_password


@app.route('/signup', methods=['POST'])
def signup():
    response = {
        "success": False,
        "message": "Invalid parameters"
    }
    try:
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(
            email=email).first()  # if this returns a user, then the email already exists in database

        if user:
            response["message"] = 'User already exists. Please Log in'
            return response, 202

        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        new_user = User(email=email, username=username, password=encrypt_string(password))
        if username == None or email == None or password == None:
            return response, 202
        if check_email(email) == False:
            response["message"] = "Invalid email!"
            return response, 202
        if checking_password(password) == False:
            response["message"] = "." \
                                  "Your password should contain at least one character from each of the following groups:" \
                                  "Lower case letter" \
                                  "Upper case letter" \
                                  "Numbers"
            return response, 202

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        response["success"] = True
        response["message"] = 'Successfully registered'
        return response, 200
    except Exception as ex:
        print(str(ex))
        return response, 422
