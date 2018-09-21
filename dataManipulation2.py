#open file and read data
try:
	with open('PT.txt') as txt_f:
		lines = txt_f.readlines()
except FileNotFoundError:
	msg = 'File dont exist.'
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
	with open('PT_reduced.txt', 'w') as hg:
		for item in x:
			hg.write("%s" % item)

#save data to .csv file
	#with open('heatGeneration2.csv', 'w') as hg:
		#for item in x:
			#hg.write("%s" % item)


