from models.transaction_model import summary, category_expenses, all_for_user
from models import user_model


def dashboard(uid):
    # Fetch logged-in user details
    user = user_model.by_id(uid)

    # Fetch income and expense summary
    sums = {
        x['type']: x['total'] or 0
        for x in summary(uid)
    }

    income = float(sums.get('income', 0))
    expense = float(sums.get('expense', 0))

    # Fetch category-wise expenses
    cats = category_expenses(uid)

    total = sum(float(x['total']) for x in cats) or 1

    for x in cats:
        x['percent'] = round(float(x['total']) * 100 / total)

    # Return dashboard data
    return {
        'user': {
            'name': user['name'] if user else 'User',
            'email': user['email'] if user else ''
        },

        'summary': {
            'income': income,
            'expenses': expense,
            'balance': income - expense
        },

        'categories': cats,

        'recent': all_for_user(uid)[:5]
    }