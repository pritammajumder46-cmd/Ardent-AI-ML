class Form:
    def __init__(self,name,age):
        self.name = name
        self.age = age

s1 = Form("Neha",18)
s2 = Form("Rohan",20)

print(s1.name,s1.age)
print(s2.name,s2.age)

try:
    class Form1:
        def __init__(name):
            name = name

    f1 = Form1("Pritam")
    print(f1.name)

except TypeError:
    print("TypeError: Use self property")