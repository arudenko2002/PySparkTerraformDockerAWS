import itertools
num = 2
ar = ['a','b','c']
a = itertools.combinations(ar, num)
rez = []
for ind in a:
    rez.append(ind)

v = set(['a'])
count=0
for ind in rez:
    b = set(ind)
    print(b, v)
    if v.issubset(b):
        count += 1

ans = 1.0*count/len(rez)
print(ans)