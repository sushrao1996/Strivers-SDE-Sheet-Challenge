def searchMatrix(mat: [[int]], target: int) -> bool:
    # Write your code here.
    i=0
    j=len(mat[0])-1
    while i<len(mat) and j>=0:
        if mat[i][j]==target:
            return True
        elif mat[i][j]<target:
            i+=1
        else:
            j-=1
    return False
    
