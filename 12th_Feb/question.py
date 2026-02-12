# TAKE A CLASS PERSON AND PASS THE PARAMETERS NAME, AGE, CITY, COUNTRY AND DISPLAY 
class Person:
    def __init__(self,name,age,city,country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

obj1 = Person("Kim",29,"Tokyo","Japan")
obj2 = Person("Pritam",20,"Khardah","India")

print(obj1.name,obj1.age,obj1.city,obj1.country)
print(obj2.name,obj2.age,obj2.city,obj2.country)

# COMPARING AGE
print(f"{obj1.name} is older") if obj1.age>obj2.age else print(f"{obj2.name} is older") if obj1.age<obj2.age else("Both are same aged")