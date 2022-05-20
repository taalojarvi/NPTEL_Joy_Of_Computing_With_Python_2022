import string
import random
bags = {}
name = string.ascii_letters

for i in range(20):
	bags[name[i]] = 0
	
for i in range(1000):
	key = random.choice(list(bags.keys()))
	bags[key] = bags[key] + 1
	
print(bags)
