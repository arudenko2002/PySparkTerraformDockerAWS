s = "there mama myla the ramu mamam myla ramy"

wordfreq = {}
for word in s.split():
    wordfreq[word] = wordfreq.setdefault(word, 0) + 1

print('\n',wordfreq)
res={}
res = {x:res.setdefault(x, 0)+1 for x in s.split()}
print(res)

from collections import Counter
print(dict(Counter(s.split())))

s2= ' '+s.strip()+' '
res = {x:s2.count(' '+x+' ') for x in s.split()}
print(res)