import functools
import time
def valid(func):
    def inner(a,b):
        if not isinstance(a,str):
            a=str(a)
        if not isinstance(b,str):
            b=str(b)
        return func(a,b)
    return inner
@valid
def fun(a:str,b:str)->str:
    return a+b
print(fun.__annotations__)
print(fun.__doc__)
print(print.__doc__)


