# Implement your function below.
def non_repeating(given_string):
    charOrder = []
    count = {}
    for i in given_string:
        if i in count:
            count[i] += 1
        else:
            count[i]=1
            charOrder.append(i)
    for i in charOrder:
        if count[i] == 1:
            return i
    return None

# NOTE: The following input values will be used for testing your solution.
non_repeating("abcab") # should return 'c'
non_repeating("abab") # should return None
non_repeating("aabbbc") # should return 'c'
non_repeating("aabbdbc") # should return 'd'