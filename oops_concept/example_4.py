class Animal:
    def __init__(self,name,color,age):
        self.__name=name 
        self.__color=color
        self.__age=age 
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,new_name):
        if isinstance(new_name, str) and new_name:
            self.__name = new_name
        else:
            print("Invalid name") 
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self,new_color):
        if isinstance(new_color, str) and new_color:
            self.__color = new_color
        else:
            print("Invalid color")

    @property
    def age(self):
        return self.__age
    def display_info(self):
        print(f"Name: {self.__name}, Color: {self.__color}, Age: {self.__age}")
    
dog=Animal("brownee","white",4)
cat=Animal("Caterpillar","black",2)
dog.display_info()
cat.display_info()
dog.name="Doberman"
dog.color="zebracross"
dog.display_info()
cat.name=""
