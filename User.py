class User():
	"""Parent class"""
	
	def __init__(self, name, surname, age='unknown'):
		"""Initialize atributes."""
		self. name = name
		self.surname = surname
		self.age = age
		self.height = 'unknown'
		
	def userData(self):
		"""Print user data."""
		print("Name: " + self.name.title() + "\nSurname: " + self.surname.title()
		+ "\nAge: " + str(self.age) + "\nHeight: " + str(self.height) + "\n")
		
	def setAge(self, age):
		"""Set user age."""
		self.age = age
	    
	def changeAge(self, age):
		"""Change age of user."""
		diff = 0
		diff = age - self.age
		self.age += diff

class Sby():
	"""Sallary by years"""
	def __init__(self, sby={'Average:':2000}):
		self.sby = sby
		self.setSby()
	
	def setSby(self):
		"""Set sby data."""	
		prompt1 = "No. of years: \n"
		years = input(prompt1)
		years = int(years)
		sby = {}
		for counter in range (0, years):
			prompt2 = "Year: "
			prompt3 = "Sallary: "
			y = input(prompt2)
			s = input(prompt3)
			sby[y] = s
		self.sby = sby
		
	def sbyReport(self):
		"""Print sby"""
		sum = 0
		i = 0
		for key, value in self.sby.items():
			k = key
			v = value
			i += 1
			sum += int(value)
			average = sum / i
			print("\nYear: " + str(k) + " Sallary: " + str(v))
			print("Average sallary: " + str(average))
		
class advancedUser(User):
	"""Child class of class User"""	
	
	def __init__(self, name, surname, age='unknown', sallary='unknown'):
		"""Initialize atributes of the parent class,
		then initialize atributes specific to advanced user"""
		super().__init__(name, surname, age='unknown')	
		
		self.sallary = sallary
		self.sby = Sby()
	
	def setSallary(self, sallary):
		"""Set sallary of user."""
		self.sallary = sallary
		
	def userData(self):
		"""Override userData method from parent class."""
		print("Name: " + self.name.title() + "\nSurname: " + self.surname.title()
		+ "\nAge: " + str(self.age) + "\nHeight: " + str(self.height) + 
		"\nSallary: " + str(self.sallary) + "\nSallary by years: " + str(self.sby)
		 + " $\n") 	

	
user1 = User('dan', 'ban')
user1.userData()

user1.setAge(21)
user1.userData()

user1.changeAge(25)
user1.userData()

user3 = User('ane', 'bell')
user3.userData()

#sby={'Average:':2000}
user4 = advancedUser('dani', 'lovato')
user4.setSallary(2000)
user4.sby.sbyReport()


		
