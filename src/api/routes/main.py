from src.api.app import app, db
from src.api.utils.helpers import token_required

from flask import render_template, request, redirect, url_for
from utils.helpers import convert_list
from models.models import Event


@app.route('/test', methods=['GET'])
@token_required
def test():
    return "Authorized"


@app.route('/notest', methods=['GET'])
def notest():
    return "No need off Authorization"


@app.route('/')
def main():
    events = Event.query.all()
    return ('')


@app.route('/event/<int:id>')
def event(id):
    event = Event.query.get(id)
    return render_template('', event=event)


@app.route('/event/<int:id>/edit')
def event_edit_page(id):
    event = Event.query.get(id)
    return render_template('', event=event)


@app.route('/event/<int:id>/update', methods=['POST'])
def event_update(id):
    event = Event.query.get(id)
    form_data = request.form
    event.title = form_data.get('title')
    event.description = form_data.get('description')
    event.date_time = form_data.get('date_time')
    event.category = form_data.get('category')
    event.link = form_data.get('link')
    db.session.add(event)
    db.session.commit()
    return redirect(url_for('event', id=id))
