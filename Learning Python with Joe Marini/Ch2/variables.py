# A global variable has scope outside of a function
# ================================================== 

a, b = 'old', 'old'
print('OUTSIDE FUNCTION - a =', a)
print('OUTSIDE FUNCTION - b =', b)

# Global vs local variables in functions
def some_function():
    # b is a global variable
    global b
    a, b = 'new', 'new'
    print('INSIDE FUNCTION - a =', a)
    print('INSIDE FUNCTION - b =', b)

some_function()
print('OUTSIDE FUNCTION - a =', a)
# Only the value of b changes as it is set to global
print('OUTSIDE FUNCTION - b =', b)
