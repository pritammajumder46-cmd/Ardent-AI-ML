# Set
# Duplicacy not allowed, Unorderd, Distinctclear

s = {'a','e','c','d','e','f'}
print(s) # Printing the set

a = {1,2,3}
b = {3,4,5}

print(a|b) # Union of a and b
print(a&b) # Intersection of a and b
print(a-b) # difference between a and b (a-b)
print(b-a) # difference between b and a (b-a)
print(a^b) # Symmetic difference between a and b [XOR] 

# Set methods
# Add, update, remove, discard, pop, clear
# Syntax - set_variable_name.methodname()


set1 = {'Salman Khan', 'Sahrukh Khan', 'Amir khan', 'Varun Dhawan'}
set2 = {'Varun Dhawan', 'Vickey Koushal', 'Ayushman Khurana'}

set1.add('Rupam Islam')
set1.add('Saswata Chaterjee') 
print(set1) # As set is orderless so .add() functions add elemnts hapazaely on the set

set1.update(set2)
print(set1) #.update() method works like union 

try:
    set2.remove('Ayushman Khurana')
    print(set2) # It removes the element given by the user
except KeyError:
    print("Since your entered vaue is not in the element set .remove() will show a keyerror")

set1.discard('Saswata Chaterjee')
print(set1) # It removes the element given by the user

set2.pop()
print(set2) # Random item will be popped because set has no fixed order

set1.clear()
print(set1) # Returns a null set [Deletes all the elements inside the set]

print("\n")

S = {'Lollipop', 'Candy', 'Marshmellow'}
for i in S:
    print(i) # Order is random because set is orderless



