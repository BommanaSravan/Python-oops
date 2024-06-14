class prac:
    def __init__(self, name, age, city):
        self.n = name
        self.a = age
        self.c = city


p = prac('sravan', 30, 'kurnool')

print(p.n, p.a, p.c)

print(getattr(p, 'a'))

setattr(p,'n','kannaya')

print(p.n, p.a, p.c)

print(p.__name__)
print(p.__dict__)
print(p.__module__)