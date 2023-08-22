class animal:
    def __init__(self,name,category):
        self.name=name
        self.category=category
    def test(self):
        print("parent class")
class dog(animal):
    def speak(self):
        print("dog name ",self.name)
class cat(animal):
    def speak(self):
        print("cat category ",self.category)
obj_dog=dog("rocky","pet")
obj_dog.test()
obj_dog.speak()
obj_cat=cat("chikku","pet")
obj_cat.test()
obj_cat.speak()