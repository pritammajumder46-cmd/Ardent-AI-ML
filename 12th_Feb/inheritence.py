# INHERITANCE[SINGLE INHERITANCE]
class Parent:
    def earn(self):
        print("Parents earn Money")
class Child(Parent):
    pass

c = Child()
c.earn()

# REAL LIFE BANK ACCOUNT EXAMPLE
# BANK DETAILS

class BankAccount():
    def __init__(self,name,account_number):
        self.name = name
        self.account_number = account_number
    def show(self):
        print(f"Name: {self.name}\nAccount Number: {self.account_number}")

class CurrentAccout(BankAccount):
    def cur(self):
        print("\nCurrent Account Details:")

class SavingsAccount(BankAccount):
    def sav(self):
        print("\nSavings Account Details:")


s = SavingsAccount("Pritam", 5323417502)
s1 = SavingsAccount("Angira", 45378964120)

s.sav()
s.show()
s1.show()

c  = CurrentAccout("Akash",102203)
c1  = CurrentAccout("Sayani",501103)

c.cur()
c.show()
c1.show()

# TYPES OF INHERITENCE
# 1. SINGLE: 1 PARENT 1 CHILD
# 2. MULTILEVEL INHERITENCE: WHEN A CHILD CLASS INHERITS ANOTHER CHILD CLASS PROPERTIES THROUGH SINGLE PARENT CLASS
class Grandfather:
    def Property(self):
        print("\nGrandfather has a house")
class Father(Grandfather):
    pass
class Son(Father):
    pass

s = Son()
s.Property()

# 3. HIERARCHICAL: 1 PARENT AND MULTIPLE CHILD CLASS

class Parent:
    def Discipline(self):
        print("Parent teaches children to be disciplined")

class Son(Parent):
    pass

class Daughter(Parent):
    pass

s = Son()
d = Daughter()

s.Discipline()
d.Discipline()