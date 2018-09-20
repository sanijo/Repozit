from random import randint

class Die():
	
	def __init__(self):
		self.side = randint(1,6)
		
	def rollDie(self):
		for i in range(10):
			self.side = randint(1,6)
			print(str(self.side))

k = Die()
k.rollDie()
