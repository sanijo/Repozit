point = {'x_position': 2, 'speed': 3}
print("Original position: " + str(point['x_position']) + "\n")
if point['speed'] < 3:
	x_inc = 1
elif point['speed'] > 3:
	x_inc = 5
else:
	x_inc = 3
point['x_position'] = point['x_position'] + x_inc
print("New position: " + str(point['x_position']) + "\n")
	
test_c = {
	'first': 'true',
	'second': 'false',
	'third': 'true',
	'fourth': 'true'
}
print("Second test: " + test_c['second'].upper() + "." )

user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
}

for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)

tests = ['first', 'second']
for name, result in test_c.items():
	print(name.title())
	if name in tests:
		print("Result of  " + name +
		" test is " + result.upper() + " .")

print("Possible results are: ")
#set is similar to a list except that each item in the set must be unique
for value in set(test_c.values()):
	print(value)

#dict in list
point1 = {'x':1, 'y':2}
point2 = {'x':3, 'y':2}
point3 = {'x':1, 'y':4}
point4 = {'x':2, 'y':2}

points_list = [point1, point2, point3, point4]

print(points_list)


#list in dict
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
	if len(languages) <= 1:
		print("\n" + name.title() + "'s favorite language is:")
		for language in languages:
			print("\t" + language.title())
	else:
		print("\n" + name.title() + "'s favorite languages are:")
		for language in languages:
			print("\t" + language.title())





















