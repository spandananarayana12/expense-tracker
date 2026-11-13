from models import user_model
from utils.validators import valid_email, clean_text


def register(name, email, password, avatar='girl'):

    name = clean_text(name)
    email = clean_text(email).lower()

    if avatar not in ('girl', 'boy'):
        raise ValueError('Please select a valid avatar.')

    if not name or not valid_email(email) or len(password or '') < 6:
        raise ValueError(
            'Enter a valid name, email and password of at least 6 characters.'
        )

    if user_model.by_email(email):
        raise ValueError('Email is already registered.')

    uid = user_model.create(name, email, password, avatar)

    return user_model.by_id(uid)


def login(email, password):

    user = user_model.by_email((email or '').lower())

    if not user or not user_model.verify(user, password):
        raise ValueError('Invalid email or password.')

    return user_model.by_id(user['id'])