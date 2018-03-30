num = 1

while num <= 10:  # Fill in the condition
  # Print num squared
  # Increment num (make sure to do this!)
  print num ** 2
  num += 1



  import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
  num = random.randint(1, 6)
  print num
  if num == 5:
    print "Sorry, you lose!"
    break
  count += 1
else:
  print "You win!"


  #While else. else is evaluated only if the while loop does not break, 
  #so once it naturally ends the while loop

d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
  # Your code here!
  print key, d[key]

  #Prints key followed by space followed by key value in dictionary


list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  # Add your code here!
  if a > b:
    print a
  else:
    print b
  
#zips creates pairs of elements when passed two lists, and stops at end of shorter one