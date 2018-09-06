def purify(numbers):
  new_list = []
  for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
      new_list.append(numbers[i])


  for num in new_list:
    print num


purify([1,2,3,4,5,6])