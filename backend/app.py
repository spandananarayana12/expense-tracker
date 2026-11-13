import os,sys
from flask import Flask,send_from_directory
from flask_cors import CORS
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from config import SECRET_KEY, DATABASE
from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp
from routes.transaction_routes import transaction_bp
from routes.budget_routes import budget_bp
from routes.report_routes import report_bp
from routes.profile_routes import profile_bp
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND=os.path.join(BASE_DIR,'frontend')
app=Flask(__name__,static_folder=FRONTEND,static_url_path='')
app.secret_key=SECRET_KEY
app.config['JSON_SORT_KEYS']=False
CORS(app,supports_credentials=True)
for bp in (auth_bp,dashboard_bp,transaction_bp,budget_bp,report_bp,profile_bp):app.register_blueprint(bp,url_prefix='/api')
@app.route('/')
def index():return send_from_directory(FRONTEND,'index.html')
@app.route('/<path:path>')
def frontend(path):
    full=os.path.join(FRONTEND,path)
    if os.path.isfile(full):return send_from_directory(FRONTEND,path)
    return send_from_directory(FRONTEND,'index.html')
print("DATABASE PATH:", os.path.abspath(DATABASE))
print("DATABASE EXISTS:", os.path.exists(DATABASE))
if __name__=='__main__':app.run(debug=False,port=int(os.getenv('PORT',5000)))
