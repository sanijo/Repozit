lst = []
lst.append("one")
lst.append("two")
lst.append("three")
print (lst)
lst.insert(0, 'zero')
print(lst)
del lst[0]
print(lst)
popedNumber = lst.pop()
print(popedNumber)
popedNumber = lst.pop(0)
print(popedNumber)
print("Invite" + " " + lst[0])
del lst[0]
lst.insert(0, "four")
print("Invite" + " " + lst[0])
lst.append("seven")
lst.append("nine")
lst.append("ten")
lst.sort()
print (lst)
for i in lst:
	print(i.title() + ", num")

squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
	k = sum(squares)
print(squares)
print(k)

new = squares[:]
new.append(11)
print(new)

available_numbers = [1, 2, 3, 4, 5]
requested_numbers = [1, 2, 6, 3]
for requested_number in requested_numbers:
	if requested_number in available_numbers:
		print("Adding " + str(requested_number) + ".")
	else:
		print("Sorry, we don't have " + str(requested_number) + ".")
print("\nFinished!")
