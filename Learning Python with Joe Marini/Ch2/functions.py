# Example file for working with functions
# ========================================

# define a basic function
def func1():
    '''prints 9'''
    print(9)
func1()

# function that takes arguments
def func2(x):
    '''prints input squared'''
    print(x**2)
func2(3)

# function that returns a value
def func3():
    '''returns 3'''
    return 3
func3()

# function with default value for an argument
def myfunc(num=2, exp=3):
    '''returns first input to the power of the second input'''
    result = num**exp
    print(result)
    return result

myfunc()     # takes default arguments
myfunc(2,10) # takes positional arguments
myfunc(exp=10, num=2) # takes keyword arguments (pos doesn't matter)
myfunc(2, exp=10) # last argument is keyword
# myfunc(num=2, 10) # SyntaxError: positional argument follows keyword argument!


# function with variable number of arguments
def func(*x):
    a,b,*c = x
    print('The first arg is', a)
    print('The second arg is', b)
    print('The last arg is', c)

func(3,5,4,6,5,2)


def multi_args(*args):
    '''returns the product of all arguments'''
    prod = 1
    for arg in args:
        prod *= arg
    return prod

print(multi_args(2,3,4))
