class Vehicle:

    def general(self):
        print("This is used for transportation")

class Car(Vehicle):
        def __init__(self):
            self.name= "i20"
            self.wheels=4

        def specific(self):
            print("This car named ",self.name, "with ",self.wheels, "wheels is used for travelling comfortably")

class Motorcycle(Vehicle):
        def __init__(self):
            self.name = "Royal"
            self.wheels = 2

        def specific(self):
            print("This bike named ",self.name, " with ", self.wheels, "wheels is used for travelling short distance")

i20 = Car()
i20.specific()
i20.general()

rf= Motorcycle()
rf.specific()
rf.general()

