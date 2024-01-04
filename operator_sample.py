class sample:
    def set_name(self,name):
        self.name=name

    def __add__(self, other):
        name = self.name + "" +other.name
        return name

first_name = sample()
second_name =sample()
first_name.set_name('Selman')
second_name.set_name('Anver')
fullname = first_name+second_name
print(fullname)
