## SPDX-License-Identifier: GPL-2.0-only

def uniqueE(L):
  freq={}
  uni=[]
  
  for item in L:
    freq[item] = freq.get(item, 0) + 1
#  print(freq)
    
  for temp in freq:
#    print(freq[temp])
    if(freq[temp]) == 1:
      uni.append(temp)
  uni.sort()
  return uni
L = [int(i) for i in input().split()]
print(uniqueE(L))
