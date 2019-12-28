import numpy as np

with open('ch3/orbits.txt', 'r') as f:
    text = f.read()

data = text.split('\n')
arr = np.array([d.split(')') for d in data])

# # Dummy data
# data = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']
# arr = np.array([item.split(')') for item in data])

def get_chain(body):
    chain = [body]
    transfers = 0
    while chain[-1] in arr[:,1]:
        chain.append(arr[arr[:,1] == chain[-1], 0][0])
        transfers += 1
    return chain, transfers

# # Day 6 Part 1
# total_transfers = 0
# for body in set(arr.ravel()):
#     c, t = get_chain(body)
#     total_transfers += t
# print(total_transfers)

# Day 6 Part 2
YOU_chain, YOU_transfers = get_chain('YOU')
SAN_chain, YOU_transfers = get_chain('SAN')

for satellite in YOU_chain:
    if satellite in SAN_chain:
        print(satellite, YOU_chain.index(satellite), SAN_chain.index(satellite))
        print('The number of orbital transfers are', YOU_chain.index(satellite) + SAN_chain.index(satellite) - 2)
        break
