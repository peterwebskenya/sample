class car:
    def __init__(self, make,model):
        self.make = make
        self.model = model

        def move(self):
            print("driving around")

class plane:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        def move(self):
            print("flying around")

class motorbike:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def move(self):
         print("ride")
#instance of our class
car = car("toyota", "markx")
plane = plane("boeing", "787")
bike = motorbike("kawasaki", "ninja650")

for i in (car, plane, bike):
    i.move()

