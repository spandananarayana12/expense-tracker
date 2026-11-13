from flask import Blueprint, request, session, jsonify

from services.auth_service import register, login

auth_bp = Blueprint('auth', __name__)


def err(e):
    return jsonify(message=str(e)), 400


@auth_bp.post('/auth/register')
def reg():

    try:
        data = request.json or {}

        u = register(
            data.get('name'),
            data.get('email'),
            data.get('password'),
            data.get('avatar', 'girl')
        )

        session['user_id'] = u['id']

        return jsonify(user=u)

    except ValueError as e:
        return err(e)


@auth_bp.post('/auth/login')
def log():

    try:
        data = request.json or {}

        u = login(
            data.get('email'),
            data.get('password')
        )

        session['user_id'] = u['id']

        return jsonify(user=u)

    except ValueError as e:
        return err(e)


@auth_bp.post('/auth/logout')
def logout():

    session.clear()

    return jsonify(message='Logged out')