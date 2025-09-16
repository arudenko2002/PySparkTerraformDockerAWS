import re
s = "aaadaa"
k = "aa"
s='aabcdeffgabcdef'
k = 'abcdef'

rez=[]
while len(s)>0:
    r = re.search(k, s)
    if r is None:
        break
    start = r.start()
    end = r.end() - 1
    #print(start, end-1, s)
    rez.append((start, end))
    s = ''.join(['x']*(start+1)) + s[start+1:]

for ind in rez:
    print(ind)

if len(rez)==0:
    print((-1,-1))