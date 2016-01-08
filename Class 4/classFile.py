def between(start, end):
	return list(map(int, range(start, end+1))) #returns list of numbers between start and end
# will eventually combine this other between() for characters for more English-like code 
def aNumber(nbr):
	return nbr.isdigit()
def getName():
	name = input('Enter a name: ')
	while not all(character.isalpha() or character.isspace() for character in name):
		name = input(str(name) + " is not a name that only contains letters or spaces, re-enter: ")
	return name
def getAge():
	age = input('Enter your age: ')
	while not aNumber(age) or float(age) not in between(0,120): #if number not between 0 and 120
		age = input(str(age) + " is not a number or reasonable age, re-enter: ")
	return float(age)
def findMax(array):
	maxNbr = max(array)
	for (index, nbr) in enumerate(array):
		if float(nbr) == maxNbr:
			return index
def getStudents(numberOfStudents):
       #maybe change to list of tuples instead of two lists
	names = []
	ages = []
	for i in range(numberOfStudents):
		names.append(getName())
		ages.append(getAge())
       return names,ages
def maxAge(names, grades):
	maxAge = findMax(ages) #returns index of highest age 
	return [names[maxAge], ages[maxAge]]