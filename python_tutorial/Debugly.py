#debugly.py
from functools import wraps
def debug(func):
    #func is function to be wrapped
    @wraps(func) #copy metedata(name, copy documentation etc) from one function to another
    def wrapper(*args,**kwargs):
     print(func.__qualname__)
     return func(*args,**kwargs)
    return wrapper
