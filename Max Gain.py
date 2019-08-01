def max_gain(input_list):
    max = input_list[1] - input_list[0]
    min = input_list[0]
    i = 1
    while i < len(input_list):
        if (input_list[i] - min > max):
            max = input_list[i] - min
        if (input_list[i] < min):
            min = input_list[i]
        i = i+1
    return 0 if max < 0 else max
# Max Gain is defined as the maxuim difference between 2 elements in the list
#such that the largest elements is after the smallest
#
# [100,40,10,5] ----> 0
# [0.50.10.100.30] -----> 100
list1 =[100,40,20,10]
list2 =[0,50,10,100,30]
list3 =[1,1]
list4 =[100,20,100]
list5 =[0,100,0,100,0,100]
list6 =[0,20,30,40,50]

print(max_gain(list1))
print(max_gain(list2))
print(max_gain(list3))
print(max_gain(list4))
print(max_gain(list5))

