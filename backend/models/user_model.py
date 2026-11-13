from werkzeug.security import generate_password_hash, check_password_hash
from utils.helpers import query, execute


def create(name, email, password, avatar='girl'):
    return execute(
        'INSERT INTO users(name, email, password_hash, avatar) VALUES(?,?,?,?)',
        (name, email, generate_password_hash(password), avatar)
    )


def by_email(email):
    return query(
        'SELECT * FROM users WHERE email=?',
        (email,),
        one=True
    )


def by_id(uid):
    return query(
        'SELECT id, name, email, avatar FROM users WHERE id=?',
        (uid,),
        one=True
    )


def verify(user, password):
    return bool(
        user and check_password_hash(user['password_hash'], password)
    )


def update(uid, name, email, password=None):
    if password:
        execute(
            'UPDATE users SET name=?, email=?, password_hash=? WHERE id=?',
            (name, email, generate_password_hash(password), uid)
        )
    else:
        execute(
            'UPDATE users SET name=?, email=? WHERE id=?',
            (name, email, uid)
        )