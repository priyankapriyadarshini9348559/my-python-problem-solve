class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"Employee Name:{self.name}")
        print(f"salary:${self.salary}")
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display(self):
        super().display()
        print(f"Department: {self.department}")
    emp1 = Employee("Amit", 40000)
    emp1.display()
    print("----------------------")

mgr1 = Manager("Priya", 75000, "HR")
mgr1.display()


        