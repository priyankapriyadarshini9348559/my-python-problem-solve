class Animal:
    def __init__(self,name,color):
        self.name=name #public
        self.__color=color #private
    @property
    def color(self):
        return self.__color
dog=Animal("brownee","white")
cat=Animal("Caterpillar","black")
print(dog.name)
print(dog.color)
print(cat.name)
print(cat.color)