a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
l=[]
s={}
for i in set(a):
    for j in set(b):

        if i == j:

            l.append(i)

            print(l)
