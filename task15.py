class Animal:
    
    def __init__(self, type, name):
        self.type = type
        self.name = name
    
    def go(self):
        print("animal goes")
        
class Cat(Animal):
    
    def __init__(self, type, name):
        super(Cat, self).__init__(type, name)
    
    def meow(self):
        print("cat meows")

class Dog(Animal):
    
    def __init__(self, type, name):
        super(Dog, self).__init__(type, name)
        
    def bark(self):
        print("dog barks")
