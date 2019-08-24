import random
import sys
a = []
with open('word1','r') as f:
    line = f.readline().strip()
    while line:
        a.append(line)
        line = f.readline().strip()
b = random.choice(a)
print(b)
i = input("your string\n")
J = 0


for l in a:
    J +=1
    if l == i:
        print("found:",l,"at",J)


