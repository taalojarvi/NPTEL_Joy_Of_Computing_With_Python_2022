L=[I for I in input().split(" ")]
#L=['ram', 'shyam', 'lakshami!']
ans=[]
final=[]

for i in L:
#   ans.append("".join(list(i)[::-1]))
  A=str(i)
  A=A[::-1]
  ans.append(A)

ans.sort()
#print (ans)

for j in ans:
#  final.append("".join(list(j)[::-1]))
  word=str(j)
  j=j[::-1]
  final.append(j)
  
print(final)
