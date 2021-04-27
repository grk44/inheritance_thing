
class vehicle:	
	def __init__(self, make, model,doors, towcap):
		self.make = make
		self.model = model
		self.doors = doors
		self.towcap=towcap

class car(vehicle):
	def __init__(self, make, model, doors):
		super().__init__(make, model,doors,doors)

class motorcycle(vehicle):
	def __init__(self, make, model):
		super().__init__(make,model,model,model)

class truck(vehicle):
	def __init__(self, make, model, doors, towcap):
		super().__init__(make, model, doors, towcap)

v1=car("Ford", "Taurus", 4)
v2=motorcycle("Honda", "NSR250R")
v3=truck("Dodge","RAM 1500", 4, "12,750 lbs")	

print("Make: {0}\nModel: {1}\nDoors:{2}".format(v1.make,v1.model,v1.doors))
print("Make: {0}\nModel: {1}".format(v2.make,v2.model))
print("Make: {0}\nModel: {1}\nDoors:{2}\nTowing Capacity:{3}".format(v3.make,v3.model,v3.doors,v3.towcap))

