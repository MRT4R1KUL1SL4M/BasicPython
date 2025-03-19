class Bike:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
    
    def __str__(self):
        return (f"Name: {self.name}, colour: {self.colour}")       
        
b1=Bike("Yamaha","Blue")
b2=Bike("Yamaha","Blue")
print(str(b1))
print(str(b2))