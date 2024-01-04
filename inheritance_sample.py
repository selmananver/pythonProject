class BaseClass:
    def __init__(self):
        print('hi')
    def display_name(self,name):
        self.name=name
        print('base class display name')

class SubClass(BaseClass):
    def __init__(self):
        super().__init__()
        print('Subclass init')
    def  welcome(self):
        print('Name is' +self.name)

    def display_name(self,name):
        super().display_name(name)
        print('sub class display name')


y= SubClass()
y.display_name('Selman')
y.welcome()