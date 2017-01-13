# Def function bubbleSort that takes in an list as a peram
# Evaluate elements against one another two at a time in chronoloigical order
# If el1 > el 2, then swap them (el2, el1 ) = (el1, el2)
# Do this until someList == sortedList
# the largest number in the pass will make its way to its right postion within that pass
#
#

import random

# A function that generates a random 100 integers between 0 and 10,000
def randomList(emptyList):

	count = 100
	for i in range(count):
		emptyList.append(random.randint(0, 10000))

	return emptyList

# A function that sorts integers in a list using the bubble sort method
def bubbleSort(getList):
	count1 = 0
	count2 = 1
	listPass =  len(getList) - 1

	while listPass >= 1:
		while count2 < len(getList):
			if getList[count1] > getList[count2]:
				getList[count2], getList[count1] = getList[count1], getList[count2]
			count1 += 1
			count2 += 1
		listPass -= 1
		count1 = 0
		count2 = 1
	return getList


# Create list that will hold a random 100 integers
newList = []

# Grab list of random integers
randomList(newList)

# Invoke bubbleSort() function and print results
print bubbleSort(newList)
