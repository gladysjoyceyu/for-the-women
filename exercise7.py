import datetime

class Car:

	def __init__(self, year, make, model):
		self.year = year
		self.make = make
		self.model = model
		
	def currentAge(self):
		now = datetime.datetime.now()
		age = now.year - self.year
		return age
		
myCar = Car(2012, "Mitsubishi", "Mirage")
print (myCar.currentAge())