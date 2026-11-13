-- Common queries
SELECT * FROM transactions WHERE user_id=? ORDER BY date DESC,id DESC;
SELECT type,SUM(amount) FROM transactions WHERE user_id=? GROUP BY type;
SELECT category,SUM(amount) FROM transactions WHERE user_id=? AND type='expense' GROUP BY category;
SELECT * FROM budgets WHERE user_id=? ORDER BY category;
