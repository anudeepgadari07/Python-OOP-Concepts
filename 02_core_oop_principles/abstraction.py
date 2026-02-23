# from abc import ABC,abstractmethod

# class vechile(ABC):

#     @abstractmethod
#     def start(self):
#         pass

# class Car(vechile):
#     def start(self):
#         pass

# c1 = Car()
# c1.start()


class Dog:
    def sounds(self):
        print("Woof!!")

class Cat:
    def sounds(self):
        print("Meows!!")

# class Animal:
#     def speak(self,entity):
#         print("animal speaks")
#         entity.sounds()

# d1=Dog()
# a1=Animal()
# a1.speak(d1)

def make_sound(animal):
    animal.sounds()

for x in [Dog(),Cat()]:
    make_sound(x)
    



