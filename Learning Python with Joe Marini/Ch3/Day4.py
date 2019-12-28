# Day 4 Part 1


def in_range(code):
    '''Returns True if code is in range 172930 - 683082'''
    return code in range(172930, 683082)


def two_adj_digits(code):
    '''Returns True if 2 adjacent digits the same'''
    code = str(code)
    for i in range(5):
        if code[i] == code[i+1]:
            return True
    return False


def digits_never_decrease(code):
    '''Returns true if digits increase or stay the same'''
    code = str(code)
    for i in range(5):
        if int(code[i]) > int(code[i+1]):
            return False
    return True


codes = range(100000, 999999)

filtered_codes = list(filter(lambda x: in_range(x) and two_adj_digits(x) and digits_never_decrease(x), codes))

print(filtered_codes[:10])
print('There are', len(filtered_codes))


# Day 4 Part 2

def two_adj_digits_no_more(code):
    '''Returns True if there are a pair of digits that is not part of a larger group of digits'''
    code = str(code)
    for i in range(1,4):
        if (code[i-1] != code[i] and code[i] == code[i+1] and code[i+1] != code[i+2]) \
        or (code[0] == code[1] and code[1] != code[2]) \
        or (code[-1] == code[-2] and code[-2] != code[-3]):
            return True
    return False


filtered_codes = list(filter(lambda x: in_range(x) and two_adj_digits_no_more(x) and digits_never_decrease(x), codes))

print(filtered_codes[:10])
print('There are', len(filtered_codes))
