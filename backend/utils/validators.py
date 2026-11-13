import re
def valid_email(email):return bool(re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$',email or ''))
def valid_amount(value):
    try:return float(value)>0
    except:return False
def clean_text(value,max_len=255):return str(value or '').strip()[:max_len]
