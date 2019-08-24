a = [0,1, 1,4, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = int(input("choose a no."))
b = []
for i in a:
    if i<=x:
        b.append(i)
print(b)
