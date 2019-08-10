#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    sums=[]
    if int(r)==1:
        for x in range(len(arr)-1):
            sums.append((x*(x+1))/2)
        return int(sum(sums))    # change in this line
    else:
        Dict={}
        Count=0
        for x in arr:

            if x in Dict:
                Dict[x]+=1
            else:
                Dict[x]=1
        for y in Dict:
            #print(y)

            if ((y % r ==0) or (y==1)) and ((y*r in Dict) and (y*r*r in Dict)):
                #print((exp_dict[y]*exp_dict[y*r]*exp_dict[y*r*r]))
                Count+=(Dict[y]*Dict[y*r]*Dict[y*r*r])
                #print("hello I am a computer nerd")

        return Count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
