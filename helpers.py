import re

def check_act(act):
    act = act.lower()
    if act == 'e':
        return 'encrypt'
    elif act == 'd':
        return 'decrypt'
    else:
        return False
    
def check_key(key):
    pattern = r'^[A-Za-z]+$' 
    if key.isalpha():
        if re.match(pattern, key):
            return True 
    else:
        return False 
    