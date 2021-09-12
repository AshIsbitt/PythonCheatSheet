# A second attempt to understaind Python decorators following Anthonywritescode Explains series 002
# https://youtu.be/WDMr6WolKUM

'''
Decorators are "syntax sugar" that tell the code to "decorate" the
f function with the dec function.
(This also works with classes somehow)
"You can attach functionality before and after an 'inner' function"
'''

import functools

def dec(func):
    # This extra decorator keeps certain important attributes from f
    @functools.wraps(func)
    def dec_inner(*args, **kwargs):
        print(f'got {args} {kwargs}')
        return func(*args, **kwargs)
    return dec_inner


@dec
def f(x):
    """This is a docstring"""
    print(f'Hello {x}')


# Decorator factory - you can also pass args to decorators


def dec2(greeting, farewell):
    def dec2_decorator(func):
        @functools.wraps(func)
        def dec2_inner(*args, **kwargs):
            print(greeting)
            ret = func(*args, **kwargs)
            print(farewell)
            return ret
        return dec2_inner
    return dec2_decorator

@dec2('hello', 'goodbye')
def f2(x: int) -> None:
    """This is a docstring"""
    print(f'Hello {x}')



#def main():
#f2(1)


#if __name__ == '__main__':
#    exit(main())

'''
Common decorators to see
- property - used on a method with no arguments (except self) to turn it into an attribute
- classmethod
- staticmethod
'''

class Cls:
    def __init__(self, x):
        self.x = x

    @property
    def y(self):
        print('Stored in Y')
        return self.x+5

    @classmethod
    def func(cls):
        print(f'in class {cls}')

    @staticmethod
    def func2():
        print('normal function')

c = Cls(5)
print(c.x)
print(c.y)

# Classmethod - these can be called on an object or a class itself
print(c.func())
print(Cls.func())

# Staticmethod
print(Cls.func2())
print(c.func2())
