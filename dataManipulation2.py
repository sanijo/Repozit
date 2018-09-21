def data_manipulation(fileName, saveName, csvName='data.csv'):
	"""Function for manipulation with .txt files."""
	
	#open file and read data
	try:
		with open(fileName) as txt_f:
			lines = txt_f.readlines()
	except FileNotFoundError:
		msg = "File " + file_name + " don't exist."
		print(msg)
	else:
		i = -1
		x = []
		for line in lines:
			i += 1
	#every i % n==0 line to save
			if i % 10 == 0: 
				x.append(lines[i])    

	#save data to .txt file
		with open(saveName, 'w') as hg:
			for item in x:
				hg.write("%s" % item)

	#save data to .csv file 
		with open(csvName, 'w') as hg:
			for item in x:
				hg.write("%s" % item)


filename = 'PT.txt'
savename = 'PT_reduced.txt'
data_manipulation(filename, savename)
