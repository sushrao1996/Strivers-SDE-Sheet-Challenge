from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :
    currsum=0
    maxsum=0
    for i in range(len(arr)):
        currsum+=arr[i]
        maxsum=max(maxsum,currsum)
        if currsum<0:
            currsum=0
    # Your code here
    # return the answer
    return maxsum
#taking inpit using fast I/O
def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
