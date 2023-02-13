class Person:
    def __init__(self, age):
        if age < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = age

    def yearPasses(self, n):
        self.age += n

    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age <= 19:
            print("You are a teenager.")
        else:
            print("You are old.")

# Create an instance of the Person class
p = Person(-1)
p.amIOld()

p = Person(4)
p.amIOld()

p = Person(10)
p.amIOld()

p = Person(16)
p.amIOld()

p = Person(18)
p.amIOld()

p = Person(64)
p.amIOld()

p = Person(38)
p.amIOld()

# Increase the age by 4 years
p.yearPasses(4)
print("Age after yearPasses:", p.age)
