import  sys
pos = 0
def search(list,n):
    l = 0
    u = len(list)-1

    while l <= u:

        mid = (u+l) // 2

        if list[mid] == n:
            globals()['pos']= mid
            return True

        else:
            if list[mid] < n:
                l = mid
            else:
                u  = mid
    else:
        sys.exit("not found")



lis = (1,2,3,5,6,7,8,9,20,56,69,78,80)
print(lis)
n = int(input("your no."))
if search(lis, n):
    print("found at", pos+1)
else:
    print("not found")