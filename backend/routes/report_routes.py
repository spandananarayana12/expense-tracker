from flask import Blueprint,request,jsonify,session
from services.report_service import report
report_bp=Blueprint('reports',__name__)
@report_bp.get('/reports')
def read():
    if not session.get('user_id'):return jsonify(message='Unauthorized'),401
    return jsonify(report(session['user_id'],request.args.get('month',''),request.args.get('category','')))
