#Classes are user defines blueprint or prototype
#Sum, multiplication,addition, constructor etc

class Calculator:
    num = 100
    #default constructor in python always constructor should always be init not like in java same to the classname
    def __init__(self,a,b):
        number=5
        #instance variables
        self.firstnumber=a   # 2   child
        self.secondnumber=b  # 10  child
        print("I am called automatically when object is created")


    def getData(self):
        print("I am now executing as method in class")

    def summation(self):
        return(self.firstnumber+self.secondnumber+Calculator.num)


obj = Calculator(2,3) #syntax for creating an object in python without adding new keyword
obj.getData()
obj.summation()


obj = Calculator(1,2)
obj.summation()

