# # POLYMORPHISM[POLY(MANY) + MORPHIC(FORMS)]
# class Bank:
#     def __init__(self, balance):
#         self.balance = balance
#     def __add__(self, other):
#         return Bank(self.balance + other.balance)
#     def __str__(self):
#         return f"Total Balance {self.balance}"

# a1 = Bank(5000)
# a2 = Bank(3000)
# print(a1 + a2)

# # Method Overloading
# class Sum:
#     def add (self,a,b):
#         return a+b
#     def add (self, a,b,c):
#         return a+b+c

# obj_sum = sum()
# print(obj_sum.add(2,3))
# print(obj_sum.add(2,3,4))

# using *kwargs for prevent method overloading

# class Sum:
#     def add(self, *numbers):
#         total = 0
#         for num in numbers:
#             total += num
#         return total

# s = Sum()
# print(s.add(2,3))
# print(s.add(2,3,4))
# print(s.add(1,2,3,4))

# POLYMORPHISM EXAMPLE
class Animal:
    def tail(self):
        print("One Tail")
    def eye(self):
        print("two eyes")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

class Cat(Animal):
    def sound(self):
        print('Cat Meows')

d = Dog()
c = Cat()

d.sound()
c.sound()
