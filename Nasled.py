class Mein():

    name='Eva'
    male='woman'

    def kyk(self, a, b):
        self.a=a
        self.b=b

class Sun(Mein):
    name = 'Dasha'
    def son(self):
        print('Солнце')

class Ted(Mein):
    def son(self):
        print('Луна')

s= Sun()
t= Ted()
s.kyk(5,10)
t.kyk(10,5)
s.son()
print(s.name)
print(t.male)
print(t.name)
print(t.male)
print(s.__dict__)
print(t.__dict__)