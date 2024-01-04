class Sampleclass:
    year=2020
    # def hello(self,n):
    #     self.name=n
    # def print_name(self):
    #     print(self.name)
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
        # print('hello')
    def add_age(self):
        self.age= self.age+1

    def relocate(self,place):
        self.place=place

    def display(self):
        print('Name' +self.name)
        print('age' +str(self.age))
        print('location ' +self.place)
        print('year' +str(Sampleclass.year))

    @classmethod

    def add_year(cls):
        cls.year =cls.year+1

    @staticmethod

    def display_welcome():
        print('welcome')
Sampleclass.display_welcome()
x= Sampleclass("Selman",20,"Aluva")
y= Sampleclass("Rohit",23,"Mumbai")
x.display()
y.display()
print('--------')
Sampleclass.year= Sampleclass.year+1
x.add_age()
y.add_age()

x.display()
y.display()
print('--------')
Sampleclass.add_year()

x.add_age()
y.add_age()
x.relocate('Mumbai')
y.relocate('Agra')

x.display()
y.display()
# name = 'Selman'
# x.hello(name)
# x.print_name()
# y.hello('Selman Anver')
# y.print_name()
# Sampleclass.hello(x)