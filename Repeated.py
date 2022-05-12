#aaaaaabbbb=a6b4

def PrintRepeated(String):
    i=0
    s=[]
    while (i<len(String)-1):
        count=1
        while String[i]==String[i+1]:
            count=count+1
            i=i+1
            if i==len(String)-1:
                break
        print(str(String[i])+str(count),end="")
        i=i+1

PrintRepeated(str(input()))