"""
Define a class named American and its subclass NewYorker.

Hints:

Use class Subclass(ParentClass) to define a subclass.

"""

class american:

    def nation(self):
        print("This is american")
class newyorker(american):
    def nation(self):
        print("This is newyorker")
obj1 = newyorker()
obj1.nation()
obj2 = american()
obj2.nation()

