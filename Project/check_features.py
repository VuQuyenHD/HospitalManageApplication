import re
from datetime import datetime

def check_file_open(filename):
    try:
        file = open(filename)
        file.close()
        return True
    except:
        return False

def check_phone(phone):
    if len(phone) ==10:
        if re.match("^\d{10}$",str(phone)):
            return True
        return False
    elif len(phone) == 12:
        if re.match("^[+]{1}\d{11}$",str(phone)):
            return True
        return False

def check_email(email):
    if len(email) <3:
        return False
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(pat,email):
        return True
    return False

def get_date(date):
    try:
        date = datetime.strptime(date,'%y-%m-%d %H:%M:%S')
        return date
    except:
        print('Error')
        return False