# Example file for working with loops

def main():

  # define a while loop
  x = 0
  while x < 5:
    print(x)
    x += 1

  
  # define a for loop
  for x in range(5, 10):
    print(x)  


  for i in range(10):
      print(i, i**3, sep=' => ', end=' | ')
      
      
  # use a for loop over a collection
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
