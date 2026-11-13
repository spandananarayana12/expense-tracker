from models.budget_model import upsert,all_for_user
from models.transaction_model import category_expenses
def save(uid,category,amount):
    if not category or float(amount)<=0:raise ValueError('Category and a positive amount are required.')
    upsert(uid,category,float(amount))
def get(uid):
    budgets=all_for_user(uid);spent={x['category']:x['total'] for x in category_expenses(uid)};items=[]
    for b in budgets:
        s=float(spent.get(b['category'],0));a=float(b['amount']);items.append({'category':b['category'],'amount':a,'spent':s,'percent':round(s*100/a) if a else 0})
    total=sum(x['amount'] for x in items);sp=sum(x['spent'] for x in items);return {'total_budget':total,'spent':sp,'remaining':total-sp,'items':items}
