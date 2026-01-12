import os
os.system("cls")

# Dictionary
# It is a python data structure working with key value pair

# dictionary = {"key1":"Value1", "key1":"Value1", ... "key_n":"Value_n",}

d = {'Virat Kohli':28000, 'Rohit Sharma': 17000, 'Hardik Pandya': 12000}
# print(d)

# properties: ordered, changable and duplication is not allowed
d = {'Virat Kohli':18000, 'Rohit Sharma': 17000, 'Hardik Pandya': 12000}
print(d)
d['Virat Kohli'] = 28000
print(d)
# d = {'Virat Kohli':18000, 'Virat Kohli': 17000, 'Hardik Pandya': 12000}
# print(d) # second key is same as first so it is replaced

for key in d.keys(): # prints the key of the dictionary
    print(key)

for value in d.values():# prints the values of the dictionary
    print(value)

for key,value in d.items():  #prints the both key and values of the dictionary
    print(f"Key = {key} & Values = {value}")

#Accessing the items of dictionary
x = d["Virat Kohli"]
y = d["Rohit Sharma"]
print(f"{x}, {y}")

# Using get() function
x1 = d.get("Hardik Pandya")
print(x1)

#Insertion
# Insertion in Dictionary process 1
d['Jasprit Bumrah'] = 3000
print(d)

# Insertion in Dictionary process 2 using .update() function
d.update({"Rabindra Jadeja": 8000})
print(d)


#Deletation
# Deletation in Dictionary using .pop() function[deletes as us like]
d.pop("Virat Kohli")
print(d)

# Deletation in Dictionary using .popitem() function[delets from last]
d.popitem()
print(d)

# d.clear() # it clears all the values of the dictionary
# del(d) # It destroys the total dictionary


# Nested Dictionary
# d = {
#     Key1 :{
#         key11 : Value11, key12 : Value12,..., key1n : Value1n, 
#     } 
#     Key2 :{
#         key21 : Value21, key22 : Value22,..., key2n : Value2n, 
#     } 
#     .
#     .
#     .
# }

cricket = {'Batsman': {'Virat':28000, 'Rohit':8000}, 'Bowler':{'Bumrah':1000, 'Jadeja':2000}}

#How can I get 28000?
print(cricket['Batsman']['Virat'])
#How can I get 1000?
print(cricket['Bowler']['Bumrah'])

#Copying a dictionary
cricket1 = d.copy() # copying a dictionary uding .copy()
cricket2 = dict(d) # copying a dictionary uding .copy()