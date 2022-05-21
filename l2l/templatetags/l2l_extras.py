from datetime import datetime

from django import template


register = template.Library()

def l2l_dt(value):
    # Expecting datetime or str, else raise TypeError
    if isinstance(value, str):
        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
    elif isinstance(value, datetime):
        pass
    else:
        raise TypeError(f'Unexpected type. Expected datetime or str, instead got {type(value)}')
    
    return value.strftime("%Y-%m-%d %H:%M:%S")

register.filter('l2l_dt', l2l_dt)
