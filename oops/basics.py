class car():
    # print("my car")
    def __init__(self, car_name, model, color):
        self.car_name = car_name
        self.model = model
        self.color = color
    def drive(self):
        print("Driving", self.car_name,self.model)
    def carname(self):
        print(self.car_name)


obj = car("vento", 2023, "grey")
print(obj.car_name)
print(obj.model)
obj.drive()
obj.carname()