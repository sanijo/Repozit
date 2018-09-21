#open file and read data
txt_f = open("data.txt", "r")
i=-1
x=[]
lines = txt_f.readlines()
for line in lines:
	i += 1
#every i % n==0 line to save
	if i % 2 == 0: 
		x.append(lines[i])    
txt_f.close()

#save data to .txt file
f = open("heatGeneration.txt", "w+")
for item in x:
	f.write("%s" % item)
f.close()

#save data to .csv file
f = open("heatGeneration.csv", "w+")
for item in x:
	f.write("%s" % item)
f.close()


