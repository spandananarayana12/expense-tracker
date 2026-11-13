from utils.helpers import query,execute
def create(uid,t):return execute('INSERT INTO transactions(user_id,type,amount,category,date,description) VALUES(?,?,?,?,?,?)',(uid,t['type'],t['amount'],t['category'],t['date'],t.get('description','')))
def all_for_user(uid):return query('SELECT * FROM transactions WHERE user_id=? ORDER BY date DESC,id DESC',(uid,))
def summary(uid):return query("SELECT type,SUM(amount) total FROM transactions WHERE user_id=? GROUP BY type",(uid,))
def category_expenses(uid):return query("SELECT category,SUM(amount) total FROM transactions WHERE user_id=? AND type='expense' GROUP BY category ORDER BY total DESC",(uid,))
def month_expenses(uid,month,category=''):return query("SELECT date,SUM(amount) total FROM transactions WHERE user_id=? AND type='expense' AND substr(date,1,7)=? AND (?='' OR category=?) GROUP BY date ORDER BY date",(uid,month,category,category))
from utils.helpers import query, execute


def create(uid, t):
    return execute(
        'INSERT INTO transactions(user_id,type,amount,category,date,description) VALUES(?,?,?,?,?,?)',
        (
            uid,
            t['type'],
            t['amount'],
            t['category'],
            t['date'],
            t.get('description', '')
        )
    )


def all_for_user(uid):
    return query(
        'SELECT * FROM transactions WHERE user_id=? ORDER BY date DESC,id DESC',
        (uid,)
    )


def summary(uid):
    return query(
        "SELECT type,SUM(amount) total FROM transactions WHERE user_id=? GROUP BY type",
        (uid,)
    )


def category_expenses(uid):
    return query(
        """
        SELECT category, SUM(amount) total
        FROM transactions
        WHERE user_id=? AND type='expense'
        GROUP BY category
        ORDER BY total DESC
        """,
        (uid,)
    )


def month_expenses(uid, month, category=''):
    return query(
        """
        SELECT date, SUM(amount) total
        FROM transactions
        WHERE user_id=?
        AND type='expense'
        AND substr(date,1,7)=?
        AND (?='' OR category=?)
        GROUP BY date
        ORDER BY date
        """,
        (uid, month, category, category)
    )


# Get expenses grouped by month
def monthly_expenses(uid, start_date, end_date, category=''):
    return query(
        """
        SELECT substr(date,1,7) AS month, SUM(amount) AS total
        FROM transactions
        WHERE user_id=?
        AND type='expense'
        AND date >= ?
        AND date < ?
        AND (?='' OR category=?)
        GROUP BY substr(date,1,7)
        ORDER BY month
        """,
        (uid, start_date, end_date, category, category)
    )