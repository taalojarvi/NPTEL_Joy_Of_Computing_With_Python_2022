## SPDX-License-Identifier: GPL-2.0-only

def all_even(L):
  for i in range(len(L)):
    if(L[i]%2==0):
      print(L[i])
L = [int(i) for i in input().split()]
all_even(L)
