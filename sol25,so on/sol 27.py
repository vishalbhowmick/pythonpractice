a = int(input("First no."))
b = int(input("Second no."))
c = int(input("Third no."))

if (a > b) & (a > c):
    print(a, " is largest no.")
elif (b > a) & (b > c):
    print(b, "is largest no.")
elif (c > a) & (c > b):
    print(c, "is largest no.")