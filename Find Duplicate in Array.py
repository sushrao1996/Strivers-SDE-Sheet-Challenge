def findDuplicate(arr:list, n:int):
    # Write your code here.
    # Returns an integer.
    res=dict()
    for i in range(len(arr)):
        if arr[i] in res:
            return arr[i]
        else:
            res[arr[i]]=1
    return 0
