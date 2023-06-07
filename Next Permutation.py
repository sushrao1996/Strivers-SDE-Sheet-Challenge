from os import *
from sys import *
from collections import *
from math import *

def nextPermutation(permutation, n):
    ind=-1
    for i in range(len(permutation)-2,-1,-1):
        if permutation[i]<permutation[i+1]:
            ind=i
            break
    if ind==-1:
        return permutation[::-1]
    j=-1
    for i in range(len(permutation)-1,-1,-1):
        if permutation[i]>permutation[ind]:
            permutation[i],permutation[ind]=permutation[ind],permutation[i]
            break
    p1=ind+1
    p2=n-1
    while p1<=p2:
        permutation[p1],permutation[p2]=permutation[p2],permutation[p1]
        p1+=1
        p2-=1
    return permutation
