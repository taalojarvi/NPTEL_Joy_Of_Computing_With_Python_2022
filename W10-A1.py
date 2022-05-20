## SPDX-License-Identifier: GPL-2.0-only

L = list(map(int, input().split()))


ans=[]
large=int(0)

for x in L:
  if (x > large):
    large = int(x)
    
for y in range(large+1):
  if y in L:
    ans.append(y)
  else:
    ans.append("0")

for z in ans:
  print(z, end=" ")
