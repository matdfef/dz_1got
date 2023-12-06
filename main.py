class Dog:
 amount_of_dogs = 0
 def init(self, size=160):
    self.size = size
    Dog.amount_of_dogs += 1
 
nick_dog = Dog()
kate_dog = Dog(size=170)
antoniovespuci_cat = Dog(size=130)
piter_cat = Dog(size=300)
print(nick_dog.size)
print(kate_dog.size)
print(antoniovespuci_cat.size)
print(piter_cat.size)
print(nick_dog.amount_of_dogs)