## SPDX-License-Identifier: GPL-2.0-only

L = [int(i) for i in input().split()]
X=sorted(L)
Y=sorted(L,reverse=True)
Small=[]
Great=[]
for i in range(3):
	Small.append(X[i])
for i in range(2):
	Great.append(Y[i])
print(Small)
print(Great)
