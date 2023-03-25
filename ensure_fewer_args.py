from functools import wraps

def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        if len(args) >2:
            return "Too many arguments!"
        return fn(*args,**kwargs)
    return wrapper  