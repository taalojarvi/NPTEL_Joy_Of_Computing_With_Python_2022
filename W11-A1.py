A=int(input())
B=int(input())
C=int(input())

longer=int(0)
num=[]
short=[]
dummy=int(0)

num.append(A)
num.append(B)
num.append(C)

for i in num:
  if (longer<i):
    longer=i
    
for j in num:
  if (longer == j):
    dummy += 1
  else:
    short.append(j)

#print(longer)
#print(short)

sqA = int(short[0] * short [0])
sqB = int(short[1] * short [1])

RHS = int(longer * longer)

LHS = sqA + sqB

if (LHS == RHS):
  print("YES",end="")
else:
  print("NO",end="")
