
code = [1, 9, 6, 9, 0, 7, 2, 0]


def gravity_assist(code):
    # Create an index that goes up in steps of 4
    for i in range(0, len(code), 4):

        # Stop if code is 99
        if code[i] == 99:
            break

        # Calculate the new code
        a, b, c = code[i+1:i+4]
        if code[i] == 1:
            code[c] = code[a] + code[b]
        else:
            code[c] = code[a] * code[b]
    return code


print(gravity_assist(code))