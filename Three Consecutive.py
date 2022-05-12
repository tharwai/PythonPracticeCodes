#three Consecutitve repetition

def CheckCons(string):
    i=0
    count=1
    while (i<len(string)-2):
        #print("i",i)
        while string[i]==string[i+1]:
            count=count+1
            i=i+1
           # print(string[i],string[i+1],i,count,"string")
            if count==3:
                return True
        i=i+1
       # print(string[i], string[i + 1], i, count,"Bahar")
    return False

if CheckCons(str("111")):
    print("Yes")
else:
    print("No")