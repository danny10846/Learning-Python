def mergeSort(alist):
  print "Splitting", alist
  if len(alist) > 1:
    mid = len(alist)//2
    leftHalf = alist[:mid]
    rightHalf = alist[mid:]
    
    mergeSort(leftHalf)
    mergeSort(rightHalf)

    mergeNow(alist, leftHalf, rightHalf)

    

  print "Merging ", alist

def mergeNow(alist, leftHalf, rightHalf):

    i = 0
    j = 0
    k = 0

    while i < len(leftHalf) and j < len(rightHalf):
      if leftHalf[i] < rightHalf[j]:
        alist[k] = leftHalf[i]
        i += 1
      else:
        alist[k] = rightHalf[j]
        j += 1
      k += 1

    while i < len(leftHalf):
      alist[k] = leftHalf[i]
      i += 1
      k += 1
    while j < len(rightHalf):
      alist[k] = rightHalf[j]
      j += 1
      k += 1




example = [54,26,93,17,77,31,44,55,20]
mergeSort(example)
print(example)