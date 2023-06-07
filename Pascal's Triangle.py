def generateRow(row):
    temp=[]
    temp.append(1)
    ans=1
    for i in range(1,row):
        ans=ans*(row-i)
        ans=ans//(i)
        temp.append(ans)
    return temp

def printPascal(n:int):
    # Write your code here.
    ans=[]
    for i in range(1,n+1):
        ans.append(generateRow(i))
    return ans
