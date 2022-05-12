#String Segmentation
def canBEsegmented(s, Dictionary):
    for i in range(1, len(s)+1):
        first = s[:i]
        if first in Dictionary:
            second = s[i:]
            if not second or second in Dictionary or canBEsegmented(second, Dictionary):
                return True
    return False


s = input()
dictionary= set(["hello","hell","on","now"])
if canBEsegmented(s,dictionary):
    print ("It can be segmented in the Dictionary Word!!!!!!!")
else:
    print("It can't be segmented in the Dictionary Word!!!!!!!")