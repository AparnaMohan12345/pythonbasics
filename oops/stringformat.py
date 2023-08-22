class rect:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def __str__(self):
        return ("rectangle with length =",{self.length} ,"and width =" ,{self.breadth})

r1 = rect(4,5)
