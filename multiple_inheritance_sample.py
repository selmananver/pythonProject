class first:
    def display(self):
        print('first')

class second:
    def display(self):
        print('second')

class Third(first,second):
    def  display1(self):
        print('Third')

x= Third()
x.display()
print(Third.mro())