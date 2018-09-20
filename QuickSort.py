def quickSort(givenList):
  quickSortHelper(givenList, 0, len(givenList)-1)

def quickSortHelper(givenList, first, last):

  if first < last:

    pivot = partition(givenList, first, last)

    quickSortHelper(givenList, first, pivot-1)
    quickSortHelper(givenList, pivot+1, last)

def partition(givenList, first, last):

  pivotValue = givenList[first]

  leftMark = first + 1
  rightMark = last

  done = False
  while not done:

    while leftMark <= rightMark and givenList[leftMark] <= pivotValue:
      leftMark += 1

    while rightMark >= leftMark and givenList[rightMark] >= pivotValue:
      rightMark -= 1

    if leftMark > rightMark:
      done = True
    else:
      temp = givenList[leftMark] 
      givenList[leftMark] = givenList[rightMark]
      givenList[rightMark] = temp

  temp = givenList[first]
  givenList[first] = givenList[rightMark]
  givenList[rightMark] = temp

  return rightMark

aList = [54,26,93,17,77,31,44,55,20]
quickSort(aList)
print(aList)
 

