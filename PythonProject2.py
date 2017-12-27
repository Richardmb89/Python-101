import math
from statistics import mode
from collections import Counter
templist = [3, 6, 7, 2, 8, 9, 2, 3, 7, 4, 5, 9, 2, 1, 6, 9, 6]

def mode(x):
    counter = Counter(x)
    max_count = max(counter.values())
    return[item for item, count in counter.items() if count == max_count]
def median(x):
    sorted_x = sorted(x)
    length_n = len(x)

    middle = length_n // 2

    if length_n % 2 == 0:
        median_Even = (sorted_x[middle - 1] + sorted_x[middle]) / 2
        return(median_Even)
    else:
        return(sorted_x[middle])
def standard_deviation(x):
    return(math.sqrt(variance(x)))

def variance(x):
    n=len(x)
    x_bar = mean(x)
    return(round(sum((x_i - x_bar)**2 for x_i in x)/(n-1),2))
def mean(x):
    sorted(x)
    return sum(x) / len(x)
sorted(templist, key=int)
print(sorted(templist))
print("mean: ", round(mean(templist), 2))
#print("median: ",median(templist))
#print("Mode: ",mode(templist))
variance(templist)
print("Standard Deviation: ", round(standard_deviation(templist), 2))
print("median: ", median(templist))
print("Mode: ", mode(templist))
print("Count the number of dupliction in the list: ", Counter(templist))
mySet = set()
dup = set()
for x in templist:
    if x in mySet:
        dup.add(x)
    else:
        mySet.add(x)
dup = list(dup)
print("All Numbers that repeat: ", dup)