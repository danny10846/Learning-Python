
#writes to output.txt file with contents of my_list
my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

for i in range(len(my_list)): 
  my_file.write(str(my_list[i]) + "\n")

my_file.close()




#############

#reads from same file
my_file = open("output.txt", "r")

print my_file.read()

my_file.close()



##########

print my_file.readline()

#reads files line by line


#standard syntax so we don't have to close every time
with open("text.txt", "w") as textfile:
  textfile.write("Success!")