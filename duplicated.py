
#Function to remove duplicates from a list using two for loops
def remove_duplicates(random_list):
  new_list = []
  for i in range(len(random_list)):
    
    if len(new_list) == 0:
      new_list.append(random_list[i])
      
    duplicated = False
    
    for j in new_list:
      if random_list[i] == j:
        duplicated = True
      
    if duplicated == False:
      new_list.append(random_list[i])
      
      
  return new_list




#Same function if I'd have known about the not in functionality of python :'(
def remove_duplicates(random_list):
  new_list = []
  for i in range(len(random_list)):
    if random_list[i] not in new_list:
      new_list.append(random_list[i])
  return new_list


