#Start from 0 
fifth_letter = "MONTY"[4]

print fifth_letter

"""len() length of string
  lower() string to lower
  upper() string to upper
  str() convert input to string 
"""

parrot = "Norwegian Blue"
print len(parrot)
print parrot.lower()
print parrot.upper()




#Adding variables to strings via %
string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

day = 6 
print "03 - %02d - 2019" % (day)


#Getting raw input from the user to store into variables
name = raw_input("What is your name? ")
quest = raw_input("What is your quest? ")
color = raw_input("What is your favorite color? ")

#Printing it back with string formatting

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)