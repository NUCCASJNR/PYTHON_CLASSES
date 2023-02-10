class Person:
    """
    A function inside a class is callled method
    """
    def __init__(self, name, birthday):
        self.name = "AlAreef"
        self.birthday =  birthday #yyyymmdd
        
    def func(self):
        print("Hello my name is " + self.name)

p1 = Person("AlAreef", 2006-6-16)
p1.func()