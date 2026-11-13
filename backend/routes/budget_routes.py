from flask import Blueprint,request,jsonify,session
from services.budget_service import save,get
budget_bp=Blueprint('budget',__name__)
@budget_bp.get('/budget')
def read():
    if not session.get('user_id'):return jsonify(message='Unauthorized'),401
    return jsonify(get(session['user_id']))
@budget_bp.post('/budgets')
def write():
    if not session.get('user_id'):return jsonify(message='Unauthorized'),401
    try:save(session['user_id'],request.json.get('category'),request.json.get('amount'));return jsonify(message='Budget saved')
    except (ValueError,TypeError) as e:return jsonify(message=str(e)),400
