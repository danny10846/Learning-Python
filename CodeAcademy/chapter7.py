prices = {"banana":4, "apple":2, "orange":1.5, "pear":3}
stock = {"banana":6, "apple":0, "orange":32, "pear":15}
#printing information in our dictionary
for key in prices:
  print key
  print "price: %s" % prices[key]
  print "stock: %s" % stock[key]





# Write your code below!
def compute_bill(food):
  total = 0 
  for i in food:
    if stock[i] > 0:
      total += prices[i]
      stock[i] -= 1
  return total


example = ["banana", "orange"]
print compute_bill(example)
    