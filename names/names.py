import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
namesDict = {}

# Already provided solution
# Found 64 duplicates
# Runtime: 14 seconds
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)


# MVP Solution
# Found 64 duplicates
# Runtime: 0.0129 seconds
for i in range(len(names_1)):
        namesDict[names_1[i]] = 0

for j in range(len(names_2)):
        if names_2[j] in namesDict:
                duplicates.append(names_2[j])


# Stretch Solution
# Found 64 duplicates
# Runtime: 0.151 seconds
names_2.sort()

def binary_search(arr, target):        
        if len(arr) == 0:
                return -1
        
        low = 0
        high = len(arr)-1
        targetFound = False
        
        while not targetFound:
                average = round((low + high) / 2)
                if arr[average] == target:
                        targetFound = True
                        return arr[average]
                elif high - low == 1:
                        break
                elif arr[average] > target:
                        high = average
                else:
                        low = average

for name in names_1:
        result = binary_search(names_2, name)
        if result == None:
                pass
        else:
                duplicates.append(result)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

