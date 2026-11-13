from flask import Blueprint,request,jsonify,session
from models.user_model import by_id,update,by_email,verify
profile_bp=Blueprint('profile',__name__)
@profile_bp.get('/profile')
def read():
    if not session.get('user_id'):return jsonify(message='Unauthorized'),401
    return jsonify(user=by_id(session['user_id']))
@profile_bp.put('/profile')
def edit():
    if not session.get('user_id'):return jsonify(message='Unauthorized'),401
    uid=session['user_id'];d=request.json;name=(d.get('name') or '').strip();email=(d.get('email') or '').strip().lower();new=d.get('new_password') or ''
    if not name or not email:return jsonify(message='Name and email are required.'),400
    existing=by_email(email)
    if existing and existing['id']!=uid:return jsonify(message='Email is already in use.'),400
    user=by_id(uid);full=by_email(user['email'])
    if new:
        if not d.get('old_password') or not verify(full,d['old_password']):return jsonify(message='Old password is incorrect.'),400
        update(uid,name,email,new)
    else:update(uid,name,email)
    return jsonify(user=by_id(uid))
