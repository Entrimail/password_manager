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
        elif len(name) < 2:
            flash('Note name is too short, minimum length is 2', category='e')
            return redirect(url_for('views.home'))
        elif len(username) < 4:
            flash('Username is too short, minimum length is 4', category='e')
            return redirect(url_for('views.home'))
        elif len(password) < 6:
            flash('Password is too short, minimum length is 6', category='e')
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
            flash('Note has been deleted', category='s')
    return jsonify({})


@views.route('/update-note', methods=['POST'])
def update_note():
    note_data = json.loads(request.data)
    if len(note_data['username']) < 4:
        flash("Note hasn't been updated, username is too short, minimum length is 4", category='e')
    elif len(note_data['password']) < 6:
        flash("Note hasn't been updated, password is too short, minimum length is 6", category='e')

    note_id = note_data['noteId']
    note = Note.query.get(note_id)
    if note and note.user_id == current_user.id and len(note_data['username']) >= 4 and len(note_data['password']) >= 6:
        if note.password == note_data['password'] and note.username == note_data['username']:
            flash("No changes", category='e')
        else:
            flash("Note has been updated, successfully", category='s')
            Note.query.filter_by(id=note_id).update({"username": note_data['username']})
            Note.query.filter_by(id=note_id).update({"password": note_data['password']})
            db.session.commit()

    return jsonify({})





