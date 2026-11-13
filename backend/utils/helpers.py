import sqlite3
from config import DATABASE
def get_db():
    conn=sqlite3.connect(DATABASE);conn.row_factory=sqlite3.Row;return conn
def query(sql,args=(),one=False):
    conn=get_db();rows=conn.execute(sql,args).fetchall();conn.close();return (dict(rows[0]) if rows else None) if one else [dict(r) for r in rows]
def execute(sql,args=()):
    conn=get_db();cur=conn.execute(sql,args);conn.commit();last=cur.lastrowid;conn.close();return last
