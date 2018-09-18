class Average():
	
	def __init__(self, data):	
		
		self.data = data
	
	def averageValue(self):
		i = 0
		summ = 0
		for member in self.data:
			summ += member
			i += 1
		average = summ / i
		print(average)
			
k = [1, 2, 3, 4, 33, 24, 100]
m = Average(k)
m.averageValue()	
