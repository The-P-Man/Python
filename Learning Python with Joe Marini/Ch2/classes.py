# Example file for working with classes
# =======================================

# Class Cars
class Cars():
  def method1(self):
    print("This is Cars method 1")

  def method2(self, someString):
    print("This is Cars method 2", someString)


# Class superCars
class superCars(Cars):
  def method1(self):
    print("This is Supercars method1")

  # ...method2 is inherited

def main():
  bmw = Cars()
  bmw.method1()
  bmw.method2('Vroom!')

  mini = superCars()
  mini.method1()
  mini.method2('Vroom squared. Inherited method 2')

if __name__ == "__main__":
  main()
