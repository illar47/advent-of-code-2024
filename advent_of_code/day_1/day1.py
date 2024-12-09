#Sort two lists of data from largest to smallest
#find differences between the two lists entries and sum it up

################################ PART 1 ################################
def sortedInsertion(arr, valToInsert): 
    arrLen = len(arr)
    if arrLen <= 0: 
        arr.append(valToInsert)
    else: 
        index = 0
        while index <arrLen and valToInsert > arr[index]: 
            index += 1
        arr.insert(index, valToInsert)

dataToSort = open('day1_input.txt', 'r') #open txt in read mode
leftSide = []
rightSide = [] 

for line in dataToSort: 
    #save to correct sets
    splitVals = line.strip().split("   ")
    sortedInsertion(leftSide, int(splitVals[0]))
    sortedInsertion(rightSide, int(splitVals[1]))

totalSum = 0
for index in range(len(leftSide)): 
    totalSum += abs(leftSide[index] - rightSide[index])

print ("Total Difference: ", totalSum, "\n")

################################ PART 2 ################################
#need to calculate count of a number's appearance in right list
totalSimilarity = 0
for value in leftSide: 
    totalSimilarity += value * rightSide.count(value)

print("Total Similarity: ", totalSimilarity, "\n")