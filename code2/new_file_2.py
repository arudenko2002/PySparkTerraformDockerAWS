#Growth Protocol
a = "abcd"

def reverse_please(a):
    return a[::-1]

def another_way(a):
    rez = ""
    for ind in range(len(a)-1,-1,-1):
        rez = rez + a[ind]
    return rez

print(reverse_please(a))
print(another_way(a))