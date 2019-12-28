#
# Example file for working with conditional statements
#

def main():
  x, y = 10, 100
    
  # Normal if elif else statement 
  if x < y: st = 'x is less than y'
  elif x == y: st = 'x is equal to y'
  else: st = 'x is greater than y'
  print(st)

  # Can use "a if C else b"
  st = 'x is greater than y' if x > y else 'x is less than or equal to y'
  print(st)



if __name__ == "__main__":
  main()

