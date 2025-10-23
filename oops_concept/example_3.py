class Animal:
    def __init__(self,name,color):
        self.name=name #public
        self.__color=color #private
    
    def get_color(self):
        return self.__color
dog=Animal("brownee","white")
cat=Animal("Caterpillar","black")
print(dog.name)
print(dog.get_color())
print(cat.name)
print(cat.get_color())