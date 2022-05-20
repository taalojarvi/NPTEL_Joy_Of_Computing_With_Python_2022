L = [int(i) for i in input().split()]
prime = int(0)
for item in L:
  counter = int(0)
  x=int(item)
  if (item == 2):
    print(item)
    break
  elif (item > 2):
    for j in range(2, x+1):
      if(x % j) == 0:
        counter=counter+1 
  if (counter == 1):
    print(x)
    break
