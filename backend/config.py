import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE=os.getenv('DATABASE_PATH',os.path.join(BASE_DIR,'expense_tracker.db'))
SECRET_KEY=os.getenv('SECRET_KEY','change-this-secret-key')
