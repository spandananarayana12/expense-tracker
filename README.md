# Expense Tracker

A Flask + SQLite expense tracker matching the supplied UI reference.

## Run

```bash
cd expense-tracker
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
pip install -r backend/requirements.txt
python - <<'PY'
import sqlite3
from backend.config import DATABASE
with open('database/schema.sql', encoding='utf-8') as f: sql=f.read()
con=sqlite3.connect(DATABASE); con.executescript(sql); con.commit(); con.close()
PY
python backend/app.py
```

Open `http://127.0.0.1:5000/`.

The frontend contains Home, Register, Login, Dashboard, Add Transaction, Budget, Reports, Profile and About pages. The separate transaction-list page is intentionally not included, following the supplied structure/reference.
