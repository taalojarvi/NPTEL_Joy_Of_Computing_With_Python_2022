def DiagCalc(M):
  row=len(M)
  column=len(M[0])
  left=int(0)
  right=int(0)
  y=int(0)
  
  for x in range(row):
    left+=M[x][x]
  
  x=int(0)
  
  for x in range(column):
#    print(row-x-1,x)
    right+=M[row-x-1][x]

#  print(M[0][2])
  print(left)
  print(right, end='')

n = int(input())
M = []
for i in range(n):
    L = list(map(int, input().split()))
    M.append(L)

DiagCalc(M)
