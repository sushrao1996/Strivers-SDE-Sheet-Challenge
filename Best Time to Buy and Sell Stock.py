from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(prices):
    # Write your code here.
    maxele=0
    maxProfit=0
    for i in range(len(prices)-1,-1,-1):
        maxele=max(maxele,prices[i])
        maxProfit=max(maxProfit,maxele-prices[i])
    return maxProfit
