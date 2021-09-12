# Python Decorators

'''
These are used to add a single line of code to change the functionality of a function
'''

def func(f):
    def wrapper():
        print("Started")
        f()
        print('ended')

    return wrapper()

def func2():
    print('f2')

@func
def func3():
    print('f3')

func2 = func(func2)
