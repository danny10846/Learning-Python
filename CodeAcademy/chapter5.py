

print 'Welcome to the Pig Latin Translator!'

#Remember colons for if statements, plus indentation is important
original = raw_input("Enter a word:")
if len(original) > 0 and original.isalpha():
  print original
else:
  print "empty"

#isalpha() returns false if we have numbers inside the string



def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print "%d squared is %d." % (n, squared)
  return squared
  
# Call the square function on line 10! Make sure to
# include the number 10 between the parentheses.

square(10)

#from math import sqrt -> lets you import one function from a module


#Some useful functions for dealing with multiple arguments
def biggest_number(*args):
  print max(args)
  return max(args)
    
def smallest_number(*args):
  print min(args)
  return min(args)

def distance_from_zero(arg):
  print abs(arg)
  return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)