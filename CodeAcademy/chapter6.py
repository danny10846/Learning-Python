zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Replace elements in the list
zoo_animals[3] = "elephant"

###########################################

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
# The first and second items (index zero and one) - > includes 0, excludes 2
first = suitcase[0:2]

###########################################

animals = "catdogfrog"
# The first three characters of animals
cat = animals[:3]
# The fourth through sixth characters
dog = animals[3:6]
# From the seventh character to the end
frog = animals[6:]

###########################################

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")
#  Found duck index, now we're inserting cobra where duck is, shifting everything to the right by 1
animals.insert(duck_index, "cobra")
print animals # Observe what prints after the insert operation

###########################################

my_list = [1,9,3,8,5,7]
for number in my_list:
  print 2*number

###########################################

#takes a list of numbers, appends the square of each one to a new list, then sorts them
start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
  square_list.append(number**2)

square_list.sort()
print square_list
###########################################

# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
print residents['Puffin'] # Prints Puffin's room number

###########################################

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['Lasagne'] = 20
menu['Beef'] = 10.50
menu['Tacos'] = 2.30
###########################################

# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
del zoo_animals['Bengal Tiger']

zoo_animals['Rockhopper Penguin'] = 'Arctic Monkeys'

############################################
inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

inventory['backpack'].sort()

inventory['backpack'].remove('dagger')
inventory['gold'] += 50

