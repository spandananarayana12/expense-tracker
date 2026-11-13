from datetime import date

from models.transaction_model import (
    month_expenses,
    monthly_expenses,
    category_expenses
)


def report(uid, month, category=''):

    # Use the current month if no month is selected
    try:
        selected = date.today().replace(
            year=int(month[:4]),
            month=int(month[5:7]),
            day=1
        ) if month else date.today().replace(day=1)

    except (ValueError, TypeError):
        selected = date.today().replace(day=1)

    # Calculate the first month in the six-month period
    month_index = selected.year * 12 + selected.month - 1 - 5

    start_year = month_index // 12
    start_month = month_index % 12 + 1

    start = date(start_year, start_month, 1)

    # Calculate the month after the selected month
    if selected.month == 12:
        end = date(selected.year + 1, 1, 1)
    else:
        end = date(selected.year, selected.month + 1, 1)

    # Get monthly expense totals
    rows = monthly_expenses(
        uid,
        start.strftime('%Y-%m-%d'),
        end.strftime('%Y-%m-%d'),
        category
    )

    # Convert database results into a dictionary
    totals = {
        row['month']: float(row['total'] or 0)
        for row in rows
    }

    # Include months with zero expenses
    labels = []
    values = []

    current = start

    while current < end:

        month_key = current.strftime('%Y-%m')

        labels.append(current.strftime('%b %Y'))
        values.append(totals.get(month_key, 0))

        # Move to the next month
        if current.month == 12:
            current = date(current.year + 1, 1, 1)
        else:
            current = date(current.year, current.month + 1, 1)

    # Get category expenses
    cats = category_expenses(uid)

    if category:
        cats = [
            x for x in cats
            if x['category'] == category
        ]

    return {
        'monthly': {
            'labels': labels,
            'values': values
        },
        'categories': cats
    }