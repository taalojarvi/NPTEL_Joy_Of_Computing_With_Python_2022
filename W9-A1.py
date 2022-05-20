def subStr(s1,s2):
  x=bool("true")
  if s2 in s1:
    x="True"
    return(x)
  else:
    x="False"
    return(x)
if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print(subStr(s1, s2))
