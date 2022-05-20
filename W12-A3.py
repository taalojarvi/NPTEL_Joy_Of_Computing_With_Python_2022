## SPDX-License-Identifier: GPL-2.0-only

L=str(input())

instit=str() 
length=len(L)
counter=int(0)
roll=str() 
for i in range(length):
  if (L[i] == "@"):
    counter=i
    break
  else:
    roll+=L[i]
    

for j in range(counter+1,length):
  if(L[j] == "."):
    break
  else:
    instit+=L[j] 
    
print(roll+" "+instit, end="" ) 
