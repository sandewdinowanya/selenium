from OOPDemo import Calculator

class Child(Calculator):

    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getCaclulatorData(self):
        return self.num + self.num2 + self.summation()  #100 200 112


obj = Child()   # invoke parent constructor
print(obj.getCaclulatorData())