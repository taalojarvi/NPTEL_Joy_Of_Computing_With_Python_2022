def Transpose(M):
N=[]
    row=len(M)
    col=len(M[0])
    for i in range(row):
    	for j in range(col):
        	N[j][i] = M[i][j]
    
    return(N)
    
n = int(input())
M = [[12,7],
    [4 ,5],
    [3 ,8]]
print(Transpose(M))
