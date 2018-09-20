def myBinarySearch(alist, element):
  first = 0
  last = len(alist)-1
  indexFound = 0

  done = False
    


  while not done and first <= last:


    midpoint = (first + last)//2
    

    if alist[midpoint] == element:
      print "Found at index %d" % midpoint
      done = True
    elif element < alist[midpoint]:
      last = midpoint - 1
      if first > last:
        print "Number not in array"
    elif element > alist[midpoint]:
      first = midpoint + 1
      if first > last:
        print "Number not in array"
      
    


      

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
myBinarySearch(testlist, 2)
myBinarySearch(testlist, 9)
myBinarySearch(testlist, 35)




