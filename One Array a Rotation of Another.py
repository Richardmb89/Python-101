# Implement your function below.
def is_rotation(list1, list2):
    if len(list1) != len(list2) or len(list2) == 0:
        return False
    if not set(list1) <= set(list2) and not set(list1) >= set(list2):
        return False
    index = 0
    while list1[0] != list2[index]:
        index+=1
    list2 = list2[index:] + list2[:index]
    index = 0
    for i in list1:
        if i != list2[index]:
            return False
        index +=1
    return True

# NOTE: The following input values will be used for testing your solution.
list1 = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
# is_rotation(list1, list2a) should return False.
list2b = [4, 5, 6, 7, 1, 2, 3]
# is_rotation(list1, list2b) should return True.
list2c = [4, 5, 6, 9, 1, 2, 3]
# is_rotation(list1, list2c) should return False.
list2d = [4, 6, 5, 7, 1, 2, 3]
# is_rotation(list1, list2d) should return False.
list2e = [4, 5, 6, 7, 0, 2, 3]
# is_rotation(list1, list2e) should return False.
list2f = [1, 2, 3, 4, 5, 6, 7]
# is_rotation(list1, list2f) should return True.
list2g = [7, 1, 2, 3, 4, 5, 6]
# is_rotation(list1, list2g) should return True.

