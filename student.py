from random import*
a = "1 year later"
class Student: 
    def init(self, height=160):
         self.height = height
    def grow(self, height):
         self.height+=height
nick = Student()
kate = Student(height=170)
nick.grow(height=randint(1, 20))
print(nick.height)
print(kate.height)
print(a)
kate.grow(height=randint(1, 20))
print(nick.height)
print(kate.height)
print(a)
nick.grow(height=randint(1, 20))
print(nick.height)
print(kate.height)
print(a)
kate.grow(height=randint(1, 20))
print(nick.height)
print(kate.height)