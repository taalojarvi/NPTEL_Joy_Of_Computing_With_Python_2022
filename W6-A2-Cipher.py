S = input()
answer=""
uppercase=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lowercase=list('abcdefghijklmnopqrstuvwxyz')
for a in S:
  if (a == " "):
  	answer+=" "
  elif a in uppercase:
    answer+=uppercase[uppercase.index(a)-3]
  elif a in lowercase:
    answer+=lowercase[lowercase.index(a)-2]
  else:
    answer += a
print(answer,end="")
