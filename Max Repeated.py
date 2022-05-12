def maxrepeated(a):
    count={x: a.count(x) for x in set(a)}
    print(max(count.values()))

maxrepeated(input())