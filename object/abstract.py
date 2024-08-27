from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def cry(self):
        pass

class Dog(Animal):
    def cry(self):
        print("わんわん")

class Cat(Animal):
    def cry(self):
        print("にゃー")
        


class Human(Animal):
    def cry(self):
        print("えーん")
    def cry(self):
        print("えーん")

cat = Cat()
cat.cry()