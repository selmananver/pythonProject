class first:
    def displayfirst(self):
        print('first')

class second(first):
    def displaysecond(self):
        print('second')

class Third(second):
    def  displaythird(self):
        print('Third')

x= Third()
x.displaythird()
x.displayfirst()