n = 5
s = "12 9 61 5 14".split()

def ispalindromic(x):
    mid = int(len(x) / 2)
    print(mid)
    ar = list(x)
    print("ar",ar)
    for i in range(mid):
        print("comp", ar, ar[i], ar[len(ar) - i-1])
        if not ar[i] == ar[len(ar) - i-1]:
            return False
    return True

print(ispalindromic('9'))
print(ispalindromic('10'))
print(ispalindromic('101'))
print(ispalindromic('1010'))


print(all([int(x)>0 for x in s]) and any([ispalindromic(x) for x in s]))