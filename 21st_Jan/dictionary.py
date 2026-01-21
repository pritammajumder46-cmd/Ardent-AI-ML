# Dictionary
# a built-in, mutable data structure that stores collections of data in key-value pairs

# Dictionary = {key:val}


student = {
    'Name' : "Pritam Majumder",
    'Age' : 21,
    'Course' : 'BCA' 
}

print(student)


student1 = {
    'Name' : 'Riya', 
    'Skills' : {
        'DBMS' : "Begineer",
        'Python' : 'Intermidiate', 

    }
}

print(student1)

print(student1['Skills']['Python']) # Skills in Python


# Create a dictionary including name, age, gender, skills - print each value using keys change one value add a new key

New_Dict = {
    'Name' : 'Misti Sarkar',
    'Age' : 20,
    'Gender' : 'Female',
    'Skills' : 'Python'

}

print(New_Dict.keys()) # Print only the key(s)
print(New_Dict.values()) # Print only the value(s)

# Printing all the values
print(f"Name :{New_Dict['Name']}")
print(f"Age :{New_Dict['Age']}")
print(f"Gender : {New_Dict['Gender']}")
print(f"Skills: {New_Dict['Skills']}")

#Changing 1 value
New_Dict['Skills'] = 'Block-Chain'
print(New_Dict)

#adding a new key
New_Dict.update({'Language':'Bengali'})
print(New_Dict)
