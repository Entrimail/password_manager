from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import db, Note
import json


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        note = Note.query.filter_by(name=name, username=username, password=password).first()
        if note:
            flash('Note already exist', category='e')
        elif len(name) < 4 or len(username) < 4 or len(password) < 4:
            flash('Note is too short', category='e')
            return redirect(url_for('views.home'))
        else:
            existing_note = Note.query.filter_by(name=name, username=username, password=password,
                                                 user_id=current_user.id).first()
            if existing_note:
                flash('Note already exist', category='e')
            else:
                new_note = Note(name=name, username=username, password=password, user_id=current_user.id)
                db.session.add(new_note)
                db.session.commit()
                flash('Note added!', category='s')
                return redirect(url_for('views.home'))

    return render_template('home.html', user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    note_id = note['noteId']
    note = Note.query.get(note_id)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})
