def bubble_sort(a_list):
    n = len(a_list)
    for i in range(n):
        for j in range(0,n-i-1):
            if a_list[j]>a_list[j+1]:
                a_list[j],a_list[j+1]=a_list[j+1],a_list[j]
    return a_list

a_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(a_list)

print("Sorted Array is : ")
for i in range(len(a_list)):
    print("%d" %a_list[i])
