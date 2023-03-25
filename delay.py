'''
@delay(3)
def say_hi():
    return "hi"

say_hi()
# should print the message "Waiting 3s before running say_hi" to the console
# should then wait 3 seconds
# finally, should invoke say_hi and return "hi"
'''

from functools import wraps
from time import sleep

def delay(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args,**kwargs):
            print("Waiting {}s before running {}".format(val,fn.__name__))
            sleep(val)
            return fn(*args,**kwargs)
        return wrapper
    return inner