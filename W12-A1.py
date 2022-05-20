## SPDX-License-Identifier: GPL-2.0-only

a=int(input())

string=[]

for x in str(a):
  string.append(x)
#  if (x != "0"):

string.reverse()

for y in string:
  print(y,end="")
