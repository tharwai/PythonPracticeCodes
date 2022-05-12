x = list(str(input()))
for i in range(1, len(x)+1):
    if x[-i] > x[-i-1]:
        x[-i], x[-i-1] = x[-i-1], x[-i]
        for j in x:
            print(j, end="")
        break
