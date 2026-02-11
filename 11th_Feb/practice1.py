# class Sum:
#     def __init__(self):
#         self.x = 10
#         self.y = 20

#     def display(self):
#         return self.x + self.y

# obj = Sum()
# print(obj.display())

# PROTECTED
# class Demo:
#     def __init__(self):
#         self._y = 20

# obj = Demo()
# print(obj._y)


# PRIVATE
# class Sample:
#     def __init__(self):
#         self.a = 10
#         self._b = 20
#         self.__c = 30

# obj = Sample()
# print(obj.a) # Public
# print(obj._b) # Private
# # print(obj.__c)
# print(obj._Sample__c) # Protected[All 3 are access modifiers]

# # NOT USING __init__
# class Person:
#     pass
# p1 = Person()
# p1.name = 'Ram'
# p1.age = 22

# print(p1.name)
# print(p1.age)

# # USING __init__
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person('Ram',22)
# print(p1.name,p1.age)

# Declaring default values
# class Person:
#     def __init__(self,name, age=12):
#         self.name = name
#         self.age = age

# p1 = Person('Neha')
# print(p1.name, p1.age)

class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 12
    def age(self):
        return self.__age

p1 = Person("Neha")
print(p1.name, p1.__age)
