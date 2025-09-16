
a = [1, 2, 3, 3, 3, 4,5,6,7]
def something_missed(a):
    return len(a)==7
def check_if_all_numbers(a):
    for ind in range(0, len(a)-1):
        if a[ind]+1 != a[ind+1]:
            return ind

def repeats(a):
    for ind in range(0, len(a) - 1):
        if a[ind+1]==a[ind]:
            return True

def repeats2(a):
    counter = dict()
    for ind in a:
        if ind in counter:
            counter[ind] += 1
        else:
            counter[ind] = 1
    for key in counter:
        if counter[key]>1:
            return True

a = b.update(c)


if something_missed(a):
    ind = check_if_all_numbers(a)
    a.insert(ind,ind-1)


# select * from symtable t1
# join symtable t2 on t1.a=t2.a and ...
# a.filter(word)

