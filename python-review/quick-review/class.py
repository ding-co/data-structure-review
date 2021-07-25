# Classes
class Greeter(object):

  # Constructor
  def __init__(self, name):
    self.name = name          # Create an instance variable

  # Instance method
  def greet(self, loud=False):
    if loud:
      print('HELLO, %s!' % self.name.upper())
    else:
      print('Hello, %s' % self.name)
  
  @staticmethod
  def f():
    print("Static (class) method")

g = Greeter('Fred')           # Construct an instance of the Greeter class
g.greet()                     # Call an instance method; Prints Hello, Fred
g.greet(loud=True)            # Call an instance method; Prints HELLO, FRED!

Greeter.f()