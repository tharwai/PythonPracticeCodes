def CheckFunction(a,N):
    obj={x: a.count(x) for x in set(a)}
    for i in obj.values():
        if i<N :
            return False
    return True
a=input()
N=int(input())
if CheckFunction(a,N):
    print("can be distributed distinctly!!!!!!")
else:
    print("Can't be distributed distinctly")