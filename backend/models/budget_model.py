from utils.helpers import query,execute
def upsert(uid,category,amount):
    row=query('SELECT id FROM budgets WHERE user_id=? AND category=?',(uid,category),one=True)
    if row:execute('UPDATE budgets SET amount=? WHERE id=?',(amount,row['id']));return row['id']
    return execute('INSERT INTO budgets(user_id,category,amount) VALUES(?,?,?)',(uid,category,amount))
def all_for_user(uid):return query('SELECT * FROM budgets WHERE user_id=? ORDER BY category',(uid,))
