from flask import Blueprint,jsonify,session
from services.dashboard_service import dashboard
dashboard_bp=Blueprint('dashboard',__name__)
@dashboard_bp.get('/dashboard')
def get():
    if not session.get('user_id'):return jsonify(message='Unauthorized'),401
    return jsonify(dashboard(session['user_id']))
