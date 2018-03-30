n = [3, 5, 7]

def total(numbers):
  result = 0
  for i in range(len(numbers)):
    result += numbers[i]
    print result
  return result

#Here we see standard looping through a list using index from 0 to length





m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists(x,y):
  return x+y

  #This will literally just append y to x 





n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
  results = []
  for numbers in lists:
    for i in numbers:
      results.append(i)
  return results
      
print flatten(n)

#Takes a list that has lists inside it, turns all numbers into one list