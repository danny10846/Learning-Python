my_dict = {
  "Name": "Danny",
  "Age" : 22,
  "Cats": 2
}

print my_dict.items()
print my_dict.keys()
print my_dict.values()

#prints out diff attributes of our dictionary


#List comprehension, specifies what you want in your list 
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

#list of even numbers squared 
even_squares = [x ** 2 for x in range(1,11) if (x % 2 == 0)]

l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2] 
#start:end:stride, prints out 3rd element to 8th in steps of 2



my_list = range(1, 11) # List of numbers 1 - 10

# This steps through from start to finish in steps of 2, starting from 1, so all odd numbers 
print my_list[::2]


my_list = range(1, 11)

# steps through a list backwards
backwards = my_list[::-1]
print backwards


my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

squares = [x ** 2 for x in range(1,11)]

print filter(lambda x: x >= 30 and x <= 70, squares)





garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = garbled[::-2]
print message