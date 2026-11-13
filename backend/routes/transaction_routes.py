from flask import Blueprint,request,jsonify,session
from services.transaction_service import add
transaction_bp=Blueprint('transactions',__name__)
@transaction_bp.post('/transactions')
def create():
    if not session.get('user_id'):return jsonify(message='Unauthorized'),401
    try:add(session['user_id'],request.json);return jsonify(message='Transaction created'),201
    except (ValueError,TypeError) as e:return jsonify(message=str(e)),400
