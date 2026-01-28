# Function

# Function with no parameter and no return value
def ABC():
    print("ABC")

ABC()
# Function with no parameter and return value

# Function with parameter and no return value
#Single Parameter
def msg (name):
    print(f"My name is {name.title()}")

my_nmae = 'pritam majumder'
msg(my_nmae)


#Multiple Parameters
def add (a,b): #Parameters
    return(a+b)

print(add(10,5)) #Arguments
#Arguments are 2 type => positional, keyword

def pet(animal, name):
    print(f"{name} is a name of a {animal}")
pet_name = 'Tommy'
pet_type = 'dog'

pet(pet_type,pet_name) #positional arguments

pet(animal='cow', name='Mahesh') # Keyword argument [for non technical background undersatndings]
# Function with parameter and return value
