# Bass Class

class Library:
    def __init__(self, title, author, publication_year):
        self.t = title
        self.a = author
        self.p = publication_year

    def get_info(self):
        print(self.t, self.a, self.p)


class Book(Library):
    def __init__(self, title, author, publication_year, genere):
        super().__init__(title, author, publication_year)
        self.g = genere

    def get_info(self):
        print(self.t, self.a, self.p, self.g)


l = Library('suits', 'harvey', 2012)

l.get_info()

b = Book('lucifer', 'devil', 2018, 'horror')

b.get_info()


#Hierarchical  inheritance

class Animal:
    def __init__(self, catagory):
        self.catagory = catagory

    def get_info(self):
        print(self.catagory)


class Dog(Animal):
    def __init__(self, catagory, name):
        super().__init__(catagory)
        self.name = name

    def get_info(self):
        print(self.catagory, self.name)


class Cat(Animal):
    def __init__(self, catagory, name):
        super().__init__(catagory)
        self.name = name

    def get_info(self):
        print(self.catagory, self.name)


a = Animal('Mammel')

a.get_info()

d = Dog('Mammel', 'dog')

d.get_info()

c = Cat('Mammel', 'cat')

c.get_info()


# Multiple Inheritance 

class Bio:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def bio_info(self):
        print(self.name, self.gender, self.age)


class emp_details():
    def __init__(self, company, emp_id):
        self.id = emp_id
        self.company = company

    def emp_info(self):
        print(self.company, self.id)


class full_details(Bio, emp_details):
    def __init__(self, name, gender, age, company, emp_id, address):
        Bio.__init__(self, name, gender, age)
        emp_details.__init__(self, company, emp_id)
        self.address = address

    def full_info(self):
        print(self.name, self.gender, self.age, self.company, self.id, self.address)


f = full_details('sravan', 'm', 20, 'wipro', 20004765, 'Kurnool')

f.full_info()
f.emp_info()
f.bio_info()


#multilevel Inheritance

class Planet:
    def __init__(self, name):
        self.name = name

    def planet_details(self):
        print(self.name)


class Country(Planet):
    def __init__(self, name, country):
        super().__init__(name)
        self.country = country

    def country_details(self):
        print(self.country)


class State(Country):
    def __init__(self, name, country, state):
        super().__init__(name, country)
        self.state = state

    def state_details(self):
        print(self.state)


s = State('Earth', 'India', 'Andhra')
s.state_details()
s.planet_details()
s.country_details()
