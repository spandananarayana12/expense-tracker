from models.transaction_model import create,all_for_user
def add(uid,data):
    if data.get('type') not in ('income','expense'):raise ValueError('Invalid transaction type.')
    amount=float(data.get('amount',0));
    if amount<=0:raise ValueError('Amount must be greater than zero.')
    if not data.get('category') or not data.get('date'):raise ValueError('Category and date are required.')
    create(uid,{**data,'amount':amount})
