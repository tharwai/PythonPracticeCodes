#Checks Prime

def checkPrime(n):
    if n==2:
        return True
    for i in range (2,n//2+1):
        if n%i:
            return True
    return False

if checkPrime(int(input())):
    print("Prime")

else:
    print("Not Prime")