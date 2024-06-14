class math:
    name = 'Sravan'

    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def multiplication(self):
        return self.a * self.b

    def add(self):
        return self.a + self.b


s = math(2, 3)
print(s.multiplication())
print(s.add())
print(s.name)
print(math.name)