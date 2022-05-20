## SPDX-License-Identifier: GPL-2.0-only

def whole(N):
  ans=int(0)
  for i in range (N+1):
    ans=ans+i
  return(ans)
N = int(input())
print(whole(N))
