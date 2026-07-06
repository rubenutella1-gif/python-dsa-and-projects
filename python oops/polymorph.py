class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model 
    def move(self):
            print("drive")
            
class boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("sail")
class plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("fly")
car1 = car("Ford", "Mustang")       #Create a Car object
boat1 = boat("Ibiza", "Touring 20") 
plane1 = plane("Boeing", "747") 
for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

    