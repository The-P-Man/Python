# If you declare a variable as global then the changes apply outside of that function

a = 'original'
b = 'original'
print('a outside is', a)
print('b outside is', b)

# Global vs. local variables in functions
def some_function():
    # "a" is a local variable
    # "b" is a global variable
    global b
    a = 'new'
    b = 'new'
    print('a has been changed to', a)
    print('b has been changed to', b)

# Only the value of b changes as it is set to global
some_function()
print('a outside is', a)
print('b outside is', b)

# Check the type
print(isinstance(a, str))
print(isinstance(a, int))

# Delete the variables
del a, b