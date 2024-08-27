from abc import ABC, abstractmethod

class Worker(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def do_work(self):
        pass

    def hello(self):
        print( f"私は {self.name} です。")
              
class Teacher(Worker):
    def do_work(self):
        print(f"{self.name} は教えた…")

class Programmer(Worker):
    def do_work(self):
        print(f"{self.name} はプログラムした…")

def instract(worker):
    worker.do_work()

teacher = Teacher("niikun")
programmer = Programmer("sankun")

instract(teacher)
instract(programmer)