# Python Data Structure
# List, Set, Tuple, Dictionary

L = ["Virat", "Rohit", "Jadeja"] # List prints as usual
S = {"Virat", "Rohit", "Jadeja"} # Set is orderless

print(L[1])
print(S)
# print(S[1])

L[1] = "Hari Sankar Roy"
L[2] = "Amrita Das"
L[0] = "Hari Sankar Roy"
print(L)

# Insert Operation
# Append, inseert, extend

L.append("Bumrah") # It is used for insert at last
print(L)

L.insert(0, "Pritam Majumder") # It is used for insert at required position
print(L)

#Extend is use for concatenate 2 lists

l1 = [1,2,3,4]
l2 = ['a','b','c']
l1.extend(l2)
print(l1)

# Delete operation
# Remove, pop, del, clear

# remove [Element wise delete]
list_1 = ["Hari Sankar Roy", "Misti Sarkar", "Shyamsundar Gayen"]
print(list_1) # Before deletation
list_1.remove("Shyamsundar Gayen")
print(list_1) # After deletation

# pop [Index wise delete]
list_1 = ["Hari Sankar Roy", "Misti Sarkar", "Amrita Das"]
print(list_1) # Before deletation
list_1.pop(1)
print(list_1) # After deletation

#del
list_2 = [10,20,30]
del list_2
# print(list_2) # It deletes the list variable totally

list_1.clear()
print(list_1) # It deletes all te elements of the list

# print the list using loop

# method 1
list_3 = [1,2,3,4,5]
for i in list_3:
    print(i)

# method 2
for i in range(0, len(list_3)):
    print(list_3[i])


# List comprehension
list_4 = [i for i in list_3] # every element of List_3 is copied at list_4
print(list_4)

# list_4.insert(0, "Amrita")
# print(list_3)
# print(list_4)

square_power = [i**2 for i in list_4 if i%2==0]
print(square_power)

#sort

list_5 = [3,2,8,7]
list_5.sort() # Sorted Assending Order
print(list_5) 
list_5.sort(reverse=True) # Sorted Descending Order
print(list_5) 

# Slicing
list_6 = [10,20,30,40,50,60]
print(list_6[1:5:1]) # prints 20 to 50
print(list_6[-1:-6:-1]) # prints 60 to 20