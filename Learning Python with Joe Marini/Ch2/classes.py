# Working with classes
# =====================

# Class 1 
class Cars():
  def method1(self):
    print("This is Cars method 1")

  def method2(self, someString):
    print("This is Cars method 2", someString)


# Class 2
class superCars(Cars):
  def method1(self):
    print("This is superCars method 1")

  # Method2 is inherited


def main():
  polo = Cars()
  polo.method1()
  polo.method2('I am a polo. Vroom!')

  ferrari = superCars()
  ferrari.method1()
  ferrari.method2('I am a ferrari. Vroom squared!')

if __name__ == "__main__":
  main()
