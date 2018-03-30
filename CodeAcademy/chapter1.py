#Print statement
print("Hello World!")
#string concatenation 
print("Hello" + "World!")




#Simple program showing basic variable calculations 
cucumbers = 3
price_per_cucumber = 3.25
total_cost = cucumbers * price_per_cucumber
print(total_cost)





#Program demonstrating how float works. 
chocs = 100
num_people = 6 

whole_chocs_per_person = chocs/num_people
print(whole_chocs_per_person)

float_chocs_per_person = chocs/float(num_people)
print(float_chocs_per_person)

""" We can use 3 quotes for multiple 
Line comments, or multiple line strings"""

#Boolean logic
basic_are_terrible = True


#Program for int, float and str casting for prints
float_1 = 0.25
float_2 = 40.0

product = float(float_1) * float(float_2)
big_string = "The product was " + str(product)


#Program summing up everything learnt in this chapter
skill_completed = "Python Syntax"
exercises_completed = 13 
points_per_exercise = 5

point_total = 100
point_total += (exercises_completed * points_per_exercise)

#The amount of points for each exercise may change, because points don't exist yet

print "I got " + str(point_total) + " points!"