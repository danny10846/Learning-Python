num  = 0b1100
mask = 0b0100
desired = num & mask

print bin(desired)

#checks if third bit from right is on or not, using the & operator



****************************

#CLASSES

class Fruit(object):
  """A class that makes various tasty fruits."""
  def __init__(self, name, color, flavor, poisonous):
    self.name = name
    self.color = color
    self.flavor = flavor
    self.poisonous = poisonous

  def description(self):
    print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

  def is_edible(self):
    if not self.poisonous:
      print "Yep! I'm edible."
    else:
      print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()


"""Python will use the first parameter that __init__() receives to refer to the object being created; 
this is why it's often called self, since this parameter gives the object being created its identity."""

class Square(object):
  def __init__(self):
    self.sides = 4

my_shape = Square()
print my_shape.sides



*********************************
#Example of inheritence from classes, returning customer object has access to its parent class, and therefore its parent classes methods
#Even if they aren't defined within the class
class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print "I'm a string that stands in for the contents of your shopping cart!"

#Returning customer inherits from parent
class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()

#We can also override methods in classes that inherit parent 

************************************

#Example showing we can still access parent classes via super method, after 
#having overridden the method prior.
class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
  
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00
  
  def full_time_wage(self, hours):
    return super(PartTimeEmployee, self).calculate_wage(hours)
  
  
  
milton = PartTimeEmployee("Milton")
print milton.full_time_wage(10)





