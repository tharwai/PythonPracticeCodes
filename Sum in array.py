# Find if sum exist or not

v = [1,2,3,4,5,6,7,8,9,10]
n = int(input())
found = set()
for i in v:
    if n-i in found:
        print( "Found and Values are :", i,"&",n-i)
        break
    else:
        found.add(i)
