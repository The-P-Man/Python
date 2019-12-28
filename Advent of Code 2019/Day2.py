# Day 2 Part 1

# code = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
# code = [1, 1, 1, 4, 99, 5, 6, 0, 99]
code = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,6,23,2,13,23,27,1,27,13,31,1,9,31,35,1,35,9,39,1,39,5,43,2,6,43,47,1,47,6,51,2,51,9,55,2,55,13,59,1,59,6,63,1,10,63,67,2,67,9,71,2,6,71,75,1,75,5,79,2,79,10,83,1,5,83,87,2,9,87,91,1,5,91,95,2,13,95,99,1,99,10,103,1,103,2,107,1,107,6,0,99,2,14,0,0]

code[1] = 12
code[2] = 2

def computer(code):
    '''Returns the code after the gravity assist computer has ran the program'''
    for i in range(0, len(code), 4):
        opcode = code[i]
        if opcode == 99:
            break
        a, b, c = code[i+1:i+4]
        if opcode == 1:
            code[c] = code[a] + code[b]
        else:
            code[c] = code[a] * code[b]
    return code

print('Part 1 answer', computer(code.copy())[0])


# Day 2 Part 2

for noun in range(1, 100):
    for verb in range(1, 100):
        code[1] = noun
        code[2] = verb
        output = computer(code.copy())
        if output[0] == 19690720:
            print('Part 2 answer', 100 * noun + verb)