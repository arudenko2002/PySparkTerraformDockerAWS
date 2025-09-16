arr = ["act", "god", "cat", "dog", "tac"]

def get_key(s):
    return ''.join(sorted(list(s)))

def group_anagrams_together_naive():
    anag = {}
    for ind in arr:
        key = get_key(ind)
        if key in anag:
            anag[key].append(ind)
        else:
            anag[key] = [ind]

    k = []
    for key in anag:
        k.append(anag[key])

    print(k)

def get_hash(s):
    max_num=26
    freq=[0]*max_num

    for c in s:
        freq[ord(c)-ord('a')] += 1

    hashList = []
    for i in range(max_num):
        hashList.append(str(freq[i]))
        hashList.append("$")
    return "".join(hashList)


def group_anagrams_together():
    mp = {}
    res = []
    for ind in arr:
        key = get_hash(ind)
        if key not in mp:
            mp[key] = len(res)
            res.append([])

        res[mp[key]].append(ind)
    return res

rs = group_anagrams_together()
print(rs)