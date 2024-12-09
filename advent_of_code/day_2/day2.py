import copy
################################ PART 1 ################################
#determine if level is safe or unsafe
# safe conditions as follows: 
# - The levels are either all increasing or all decreasing.
# - Any two adjacent levels differ by at least one and at most three.
# determine total count of safe reports 
print("-----------------------------PART 1 RESULTS -----------------------------")
safeReportsCount = 0
unsafeReports = []

data = open('day2_sucessEdge.txt', 'r') #open txt in read mode
def isInc(val):
    if val < 0: 
        return False
    else: 
        return True
def validDiff(val): 
    toCompare = abs(val)
    return toCompare >= 1 and toCompare <= 3
#full logic
totLines = 0
for line in data: 
    totLines += 1
    status = False
    vals_str = line.split(" ")
    
    vals = [int(x) for x in vals_str]
    valLen = len(vals)
    for index in range(valLen):
        #edge case - at start
        if index <= 0: 
            diff = vals[index] - vals[index + 1]
            if not validDiff(diff):
                unsafeReports.append([index,vals])
                break
            status = isInc(diff)
        #standard logic
        elif index > 0 and index <= valLen - 2:
            diff = vals[index] - vals[index + 1]
            if not validDiff(diff) or (isInc(diff) != status): 
                unsafeReports.append([index + 1,vals])
                break
        #edge case - at end
        else:
            diff = vals[index - 1] - vals[index]
            if validDiff(diff) and (isInc(diff) == status): 
                safeReportsCount += 1
            else:
                unsafeReports.append([index,vals])

print("Total Safe Reports: ", safeReportsCount)
print("Total Number of Lines: ", totLines)

################################ PART 2 ################################
#dampener thingy - same as above but now if we remove one condition it will still pass
print("-----------------------------PART 2 RESULTS -----------------------------")
dampenerSafeReportsCount = 0

for report in unsafeReports: 
    
    oldReport = copy.deepcopy(report[1])
    print(oldReport)
    report[1].pop(report[0])
    print("index: ", report[0])
    vals = report[1]
    
    valLen = len(vals)
    for index in range(valLen):
        #edge case - at start
        if index <= 0: 
            diff = vals[index] - vals[index + 1]
            if not validDiff(diff):
                print("--------failure report--------")
                print("    Old Report: ", oldReport)
                print("    New Report: ", vals)
                break
            status = isInc(diff)
        #standard logic
        elif index > 0 and index <= valLen - 2:
            diff = vals[index] - vals[index + 1]
            if not validDiff(diff) or (isInc(diff) != status): 
                print("--------failure report--------")
                print("    Old Report: ", oldReport)
                print("    New Report: ", vals)
                break
        #edge case - at end
        else:
            diff = vals[index - 1] - vals[index]
            if validDiff(diff) and (isInc(diff) == status): 
                dampenerSafeReportsCount += 1
                print("    SUCESS")
            else: 
                print("--------failure report--------")
                print("    Old Report: ", oldReport)
                print("    New Report: ", vals)

print("TOTAL DAMPNER RESULTS: ", dampenerSafeReportsCount + safeReportsCount)