## SPDX-License-Identifier: GPL-2.0-only

a=int(input())
b=int(input())

comp=[]
prime=[]

count=int(0)

for x in range(a,b+1):
  count=int(0)
  
  for y in range (2,x+1):
    if(x % y == 0):
      count += 1
      
  if(count >= 2):
    print(x)
