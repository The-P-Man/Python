# Example file for helloworld
def main():
  '''This function prints "Hello world!"'''
  print ("Hello, World!")
    
    
  # Print The Times Tables from 1 to 10
  rng = range(1, 11) 
  
  print()
  print('\t|', end='\t')
  for h in rng:
    print(h, end='\t')
  print('\n------------------------------------------------------------------------------------------')
  for i in rng:
    print(i, end='\t|\t')
    for j in rng:
      print(i*j, end='\t')
    print()

# Execute the main function if and only if this file is run directly (and not called from another file)
if __name__ == "__main__":  # Evaluates to True if file is executed itself
  main()                    # Run the main function


