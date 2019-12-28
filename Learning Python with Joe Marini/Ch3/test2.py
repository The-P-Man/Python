from random import randint

def get_number(x):
    for i in range(x):
        print(i)
        if i:
            return i
    return i

print(get_number(100))