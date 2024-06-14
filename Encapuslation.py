class Myclass:
    def __init__(self):
        self.public =10
        self.protected=20
        self.private=30

    def public_att(self):
        return self.public
    def _protected_att(self):
        return self.protected
    def __private_att(self):
        return self.private

m=Myclass()
print(m.public_att())
print(m._protected_att())
print(m.__private_att())
