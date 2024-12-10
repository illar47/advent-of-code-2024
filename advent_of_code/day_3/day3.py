import re
################################ PART 1 ################################
#perform only valid mult operations mult(9, 8) - skip invalid operations
#What do you get if you add up all of the results of the multiplications?
print("-----------------------------PART 1 RESULTS -----------------------------")

data = open('day3_input.txt', 'r') #open txt in read mode
validCommandRegex = r"(mul\(\d+,\d+\))" #"mul(\d+,\d+)" #need it to specifically check for numeric values mul\()(\)
digitFinderRegex = r"(\d+),(\d+)"
finalTot = 0
for line in data: 
    validOperations = re.findall(validCommandRegex, line)
    for oper in validOperations: 
        digitList = re.findall(digitFinderRegex, oper)
        for digits in digitList:
            finalTot += (int(digits[0]) * int(digits[1]))

print("Part 1 Final Total: ", finalTot)

################################ PART 2 ################################
#adding in a new feature: 
#The do() instruction enables future mul instructions.
# The don't() instruction disables future mul instructions.
# multiplication starts in an enabled state
print("-----------------------------PART 2 RESULTS -----------------------------")

data = open('day3_test.txt', 'r') #open txt in read mode
validCommandRegex = r"(mul\(\d+,\d+\))" #"mul(\d+,\d+)" #need it to specifically check for numeric values mul\()(\)
digitFinderRegex = r"(\d+),(\d+)"
enable = True
finalTot = 0
for line in data: 
    validOperations = re.findall(validCommandRegex, line)
    for oper in validOperations: 
        digitList = re.findall(digitFinderRegex, oper)
        for digits in digitList:
            finalTot += (int(digits[0]) * int(digits[1]))

print("Part 2 Final Total: ", finalTot)