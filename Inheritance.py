class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print('make genric sound')


class Dog(Animal):
    def __init__(self, species, type):
        super().__init__(species)
        self.type = type

    def make_sound(self):
        print(f'{self.species},{self.type}')


a = Animal('generic')

# a.make_sound()
#
# d = Dog('Animal', 'Kukka')
# d.make_sound()
print(a)


# Create a base class called Person with attributes name and age in constructor . Then, create a derived class called
# Employee that inherits from Person and adds an additional attribute employee_id in constructor. Create an instance 
# of the Employee class and print out its name, age, and employee ID.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        print(self.name, self.age)


class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def print_details(self):
        print(self.name, self.age, self.employee_id)


p = Person('sravan', 30)

p.print_details()

e = Employee('kannya', 4, 1)

e.print_details()
