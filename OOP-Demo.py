#Classes are user defines blueprint or prototype
#Sum, multiplication,addition, constructor etc

class Calculator:
    num = 100
    #default constructor in python always constructor should always be init not like in java same to the classname
    def __init__(self):
        print("I am called automatically when object is created")


    def getData(self):
        print("I am now executing as method in class")


obj = Calculator() #syntax for creating an object in python without adding new keyword
obj.getData()

print(obj.num)

