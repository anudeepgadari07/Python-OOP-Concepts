''' The word Polymorphism means "many forms" and it allows object of different classes
to be treated through same interface while producing different behaviours .
-> same interface ,different method
'''

## Basic Example of how Polymorphism works:
# class Dog:
#     def sounds(self):
#         print("Dog Woofs!!")

# class Cat:
#     def sounds(self):
#         print("cat Meows!!")

# def make_sound(animal):
#     animal.sounds()

# make_sound(Dog()) #output: Dog Woofs!!
# make_sound(Cat()) #output: Cat meaws!!
## observe carefully here different behaviours for different objects but same method call

'''Method Overriding (Runtime polymorphism) - A Parent class defines a method and Chilld classes override it,
calling the method on different objects give different result.'''

# class A:
#     def show(self):
#         print("from A")

# class B(A):
#     def show(self):
#         print("from B")
# obj = B()
# obj.show() ##output : from B
## Here it parent has show() method but it prints its own method which is in class B.
## it overrides it parent method and python resolves it using MRO at runtime.
## this is runtime polymorphism , Decision happens at runtime based on object type.

'''Duck Typing - Duck typing in Python is a form of polymorphism where an object's behavior determines its 
usability rather than its actual type, following the principle “if it behaves like a duck, it is treated as a duck.” '''
# class Company: #Duck
#     def build(self):
#         print("builds s/w.")

# class Laptop: #Duck
#     def build(self):
#         print("in laptop..")

# class Coders:
#     def code(self,machine):
#         print("coders code...")
#         machine.build()
        
# co = Company()
# l1 = Laptop()

# c1 = Coders()
# # c1.code(l1)
# c1.code(co)
''' Python does not care about the object’s type.
Python only cares whether the object has the required method/behavior
⚖️ Pros of Duck Typing
✅ Very flexible
✅ Less boilerplate
✅ Cleaner code
✅ Encourages polymorphism
✅ Works without inheritance

⚠️ Cons of Duck Typing
❌ Errors appear at runtime
❌ Harder for beginners to debug
❌ Less strict than static typing
❌ IDE autocomplete weaker (without hints)
 '''
## --------------------------------------------------------------------------------

''' Operater Overloading :- Operator overloading allows the same operator to behave differently depending on the operands.
print(5 + 3)          # integer addition
print("hi" + "bye")   # string concatenation
print([1] + [2])      # list merge
Same operator (+) → different behavior.

How Python Implements It:
Python uses special magic methods (dunder methods).
When you write:
a + b

Python actually calls:
a.__add__(b)

'''
class Bank:
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
    def __add__(self,other):
        if isinstance(other,Bank):      
            return Bank(
                name=f"{self.name}&{other.name}",
                balance=self.balance+other.balance
            )
    
    def view_balance(self):
        return f"{self.balance}"
a1 = Bank("Anu",1000)
a2 = Bank("elizi",2000)
# print(a2.view_balance()) #it prints 2000 as expected
combained = a1 + a2
print(combained.view_balance())