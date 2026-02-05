class Person:
    def __init__(self,age):
        self._age = age


    def get_age(self):
        return self._age


    def set_age(self, value):
        if value < 0:
            print("Varsta invalida")
            return
        self._age = value

p = Person(25)

print(p.get_age())
p.set_age(30)

