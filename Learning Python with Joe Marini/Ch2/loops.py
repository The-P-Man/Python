# Working with loops

def main():

  # define a while loop
  x = 0
  while x < 3:
    print('x < 3', x)
    x += 1
  else:
    print('x >= 3', x)

  
  # define a for loop
  rng = range(1,4)
  for x in rng:
    print(rng, x)
  else:
    print(rng, 'ended at', x)

  for i in range(10):
      print(i, i**3, sep=' => ', end=' | ')
  else:
    print(i + 1, (i + 1)**3, sep=' => ')    
      
  # use a for loop over a list
  zoo = ['elephant', 'lion', 'oryx', 'dikdik', 'zebra']

  for animal in zoo:
    print(animal)


  # Using the enumerate() function to get index 
  days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]   

  for i, day in enumerate(days):
    print(i, day) 
    

  # use the continue and break statements
  for x in range(10):
    if x == 3:          # if 3 skip to next iteration
      continue
    if x == 6:          # if 6 break the loop
      break
    print(x, end=', ')
  print()


if __name__ == "__main__":
  main()
