class Sunrise:
    def kok(self,a,b):
        self.a=a
        self.b=b

class Son(Sunrise):
    def ok(self,c):
        self.c=c

m=Sunrise()
n=Son()
print(m.kok(4,5))
print(n.ok(6))
print(m.__dict__)
print(n.__dict__)