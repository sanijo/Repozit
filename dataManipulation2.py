#open file and read data
with open('data.txt') as txt_f:
	i=-1
	x=[];
	lines = txt_f.readlines()
	for line in lines:
		i += 1
#every i % n==0 line to save
		if i % 100 == 0: 
			x.append(lines[i])    

#save data to .txt file
with open('heatGeneration2.txt', 'w+') as hg:
	for item in x:
		hg.write("%s" % item)

#save data to .csv file
with open('heatGeneration2.csv', 'w+') as hg:
	for item in x:
		hg.write("%s" % item)


