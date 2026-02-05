class Person:
    def __init__(self,age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            print("Varsta invalida")
            return
        self._age = value

p = Person(25)

print(p.age) # citire (getter)

p.age = 30   # modificare (setter)
print(p.age)

p.age = -5   # nu se modifica
print(p.age)