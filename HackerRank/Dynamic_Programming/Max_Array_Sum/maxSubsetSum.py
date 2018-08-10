#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    n=len(arr)
    # sp[i] = sum when arr[i] is Present
    # sa[i] = sum when arr[i] is Not Present
    # ans should be max(sp[0],sa[0])
    sp=[arr[i] for i in range(n)]
    sa=[0 for i in range(n)]
    i=n-1
    while i>=0:
        sa[i-1]= max(sp[i],sa[i])
        sp[i-1]=arr[i-1]+sa[i]
        i=i-1
    return(max(sp[0],sa[0]))    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
