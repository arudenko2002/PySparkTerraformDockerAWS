import itertools
import operator
from itertools import groupby


def accumulate_func():
    data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
    print("data = ", data)
    rez = list(itertools.accumulate(data))
    print("accumulate(data)=", rez)
    rez = list(itertools.accumulate(data, max))
    print("accumulate(data, max)=",rez)
    # accumulate(data, max), [3, 4, 6, 6, 6, 9, 9, 9, 9, 9]
    rez = list(itertools.accumulate(data, operator.mul))
    print("accumulate(data, operator.mul)=", rez)
    #[3, 12, 72, 144, 144, 1296, 0, 0, 0, 0]

    # Amortize a 5% loan of 1000 with 10 annual payments of 90
    update = lambda balance, payment: round(balance * 1.05) - payment
    rez = list(itertools.accumulate(itertools.repeat(90, 10), update, initial=1000))
    a = itertools.repeat(90, 5)
    for ind in a:
        print(ind)

    print("list(map(update, [2,2,2], [1,1,1]))=", list(map(update, [2,2,2], [1,1,1])))
    # list(map(update, [2,2,2], [1,1,1]))= [1, 1, 1]
    print("accumulate(itertools.repeat(90, 10), update, initial=1000 =", rez)
    #accumulate(itertools.repeat(90, 10), update, initial=1000 = [1000, 960, 918, 874, 828, 779, 728, 674, 618, 559, 497]

# accumulate_func()

def batched_func():
    data =['roses', 'red', 'violets', 'blue', 'sugar', 'sweet']
    a = list(itertools.batched(data, 2))
    print("batched(data), 2) = ", a)
    # batched(data), 2) = [('roses', 'red'), ('violets', 'blue'), ('sugar', 'sweet')]

batched_func()

def chain_func():
    data = "ABC"
    data2 = "DEF"
    data3 = "GHI"
    a = itertools.chain(data, data2, data3)
    for ind in a:
        print("chain(data, data2, data3) = ", ind)
    # A B C D E F G H I

# chain_func()

def from_iterable():
    data = "ABC"
    data2 = "DEF"
    data3 = "GHI"
    a = itertools.chain(data, data2, data3)
    for ind in a:
        print("chain(data, data2, data3) = ", ind)
    # same as chain
    # A B C D E F G H I

#from_iterable()

def combinations_func():
    data = "ABCD"
    a = itertools.combinations(data, 2)
    for ind in a:
        print("combinations(data, 2)",ind)
    a = itertools.combinations(data, 3)
    for ind in a:
        print("combinations(data, 3)", ind)
    a = itertools.combinations(data, 4)
    for ind in a:
        print("combinations(data, 2)", ind)
    # combinations(data, 2) ('A', 'B')
    # combinations(data, 2) ('A', 'C')
    # combinations(data, 2) ('A', 'D')
    # combinations(data, 2) ('B', 'C')
    # combinations(data, 2) ('B', 'D')
    # combinations(data, 2) ('C', 'D')
    # combinations(data, 3) ('A', 'B', 'C')
    # combinations(data, 3) ('A', 'B', 'D')
    # combinations(data, 3) ('A', 'C', 'D')
    # combinations(data, 3) ('B', 'C', 'D')
    # combinations(data, 2) ('A', 'B', 'C', 'D')

#combinations_func()

def combinations_with_replacement_func():
    data = 'ABC'
    b = itertools.combinations(data, 2)
    for ind in b:
        print('itertools.combinations(data, 2)=', ind)
    a = itertools.combinations_with_replacement(data, 2)
    for ind in a:
        print('itertools.combinations_with_replacement(data, 2)=', ind)
    a = itertools.combinations_with_replacement(data, 3)
    for ind in a:
        print('itertools.combinations_with_replacement(data, 3)=', ind)
    a = itertools.combinations_with_replacement(data, 4)
    for ind in a:
        print('itertools.combinations_with_replacement(data, 4)=', ind)
    # itertools.combinations(data, 2) = ('A', 'B')
    # itertools.combinations(data, 2) = ('A', 'C')
    # itertools.combinations(data, 2) = ('B', 'C')
    # itertools.combinations_with_replacement(data, 2) = ('A', 'A')
    # itertools.combinations_with_replacement(data, 2) = ('A', 'B')
    # itertools.combinations_with_replacement(data, 2) = ('A', 'C')
    # itertools.combinations_with_replacement(data, 2) = ('B', 'B')
    # itertools.combinations_with_replacement(data, 2) = ('B', 'C')
    # itertools.combinations_with_replacement(data, 2) = ('C', 'C')
    # itertools.combinations_with_replacement(data, 3) = ('A', 'A', 'A')
    # itertools.combinations_with_replacement(data, 3) = ('A', 'A', 'B')
    # itertools.combinations_with_replacement(data, 3) = ('A', 'A', 'C')
    # itertools.combinations_with_replacement(data, 3) = ('A', 'B', 'B')
    # itertools.combinations_with_replacement(data, 3) = ('A', 'B', 'C')
    # itertools.combinations_with_replacement(data, 3) = ('A', 'C', 'C')
    # itertools.combinations_with_replacement(data, 3) = ('B', 'B', 'B')
    # itertools.combinations_with_replacement(data, 3) = ('B', 'B', 'C')
    # itertools.combinations_with_replacement(data, 3) = ('B', 'C', 'C')
    # itertools.combinations_with_replacement(data, 3) = ('C', 'C', 'C')
    # itertools.combinations_with_replacement(data, 4) = ('A', 'A', 'A', 'A')
    # itertools.combinations_with_replacement(data, 4) = ('A', 'A', 'A', 'B')
    # itertools.combinations_with_replacement(data, 4) = ('A', 'A', 'A', 'C')
    # itertools.combinations_with_replacement(data, 4) = ('A', 'A', 'B', 'B')
    # itertools.combinations_with_replacement(data, 4) = ('A', 'A', 'B', 'C')
    # itertools.combinations_with_replacement(data, 4) = ('A', 'A', 'C', 'C')
    # itertools.combinations_with_replacement(data, 4) = ('A', 'B', 'B', 'B')
    # itertools.combinations_with_replacement(data, 4) = ('A', 'B', 'B', 'C')
    # itertools.combinations_with_replacement(data, 4) = ('A', 'B', 'C', 'C')
    # itertools.combinations_with_replacement(data, 4) = ('A', 'C', 'C', 'C')
    # itertools.combinations_with_replacement(data, 4) = ('B', 'B', 'B', 'B')
    # itertools.combinations_with_replacement(data, 4) = ('B', 'B', 'B', 'C')
    # itertools.combinations_with_replacement(data, 4) = ('B', 'B', 'C', 'C')
    # itertools.combinations_with_replacement(data, 4) = ('B', 'C', 'C', 'C')
    # itertools.combinations_with_replacement(data, 4) = ('C', 'C', 'C', 'C')

#combinations_with_replacement_func()

def compress_func():
    data = 'ABCDEF'
    selectors = [1, 0, 1, 0, 1, 1]
    a = itertools.compress(data, selectors)
    for ind in a:
        print('compress(data, selectors)=', ind)

# compress_func()

def count_func():
    start = 10
    a = itertools.count(start)
    for ind in a:
        print('count(data)=', ind)
        if ind == 15:
            break

    start = 2.5
    step = 0.5
    a = itertools.count(start, step)
    for ind in a:
        print('count(data, step)=', ind)
        if ind == 15:
            break

# count(data)= 10
# count(data)= 11
# count(data)= 12
# count(data)= 13
# count(data)= 14
# count(data)= 15
# count(data, step)= 2.5
# count(data, step)= 3.0
# count(data, step)= 3.5
# count(data, step)= 4.0
# count(data, step)= 4.5
# count(data, step)= 5.0
# count(data, step)= 5.5
# count(data, step)= 6.0
# count(data, step)= 6.5
# count(data, step)= 7.0
# count(data, step)= 7.5
# count(data, step)= 8.0
# count(data, step)= 8.5
# count(data, step)= 9.0
# count(data, step)= 9.5
# count(data, step)= 10.0
# count(data, step)= 10.5
# count(data, step)= 11.0
# count(data, step)= 11.5
# count(data, step)= 12.0
# count(data, step)= 12.5
# count(data, step)= 13.0
# count(data, step)= 13.5
# count(data, step)= 14.0
# count(data, step)= 14.5
# count(data, step)= 15.0

# count_func()

def cycle_func():
    data = 'ABC'
    a = itertools.cycle(data)
    iter=0
    for ind in a:
        print(ind)
        if iter>10:
            break
        iter += 1
# A
# B
# C
# A
# B
# C
# A
# B
# C
# A
# B
# C

# cycle_func()

def dropwhile_func():
    predicate = lambda x: x<5  # drop all elements < 5
    data = [1,4,6,3,8]
    a = itertools.dropwhile(predicate, data)
    for ind in a:
        print(ind)

# 6
# 3
# 8

# dropwhile_func()

def filterfalse_func():
    predicate = lambda x: x<5  # drop all elements < 5
    data = [1,4,6,3,8]
    a = itertools.filterfalse(predicate, data)
    for ind in a:
        print(ind)
# 6
# 8

#filterfalse_func()

def groupby_func():
    data = 'AAAABBBCCDAABBB'
    a =  groupby(data)
    print(a)
    for ind in a:
        ar = [x for x in ind[1]]
        print("key=", ind[0], "length=", len(ar))
# key= A length= 4
# key= B length= 3
# key= C length= 2
# key= D length= 1
# key= A length= 2
# key= B length= 3
    data2 = [1, 1, 1, 1, 2, 2, 3]
    a = groupby(data2)
    print(a)
    for ind in a:
        ar = [x for x in ind[1]]
        print("key=", ind[0], "length=", len(ar))
# key= 1 length= 4
# key= 2 length= 2
# key= 3 length= 1
#groupby_func()

def islice_func():
    data = 'ABCDEFG'
    a = itertools.islice(data, 2)
    for ind in a:
        print('islice(data, 2)', ind)

    a = itertools.islice(data, 2, 4)
    for ind in a:
        print('islice(data, 2, 4)', ind)

    a = itertools.islice(data, 2, None)
    for ind in a:
        print('islice(data, 2, None)', ind)

    a = itertools.islice(data, 2, None, 2)
    for ind in a:
        print('islice(data, 2, None, 2)', ind)

# islice(data, 2) A
# islice(data, 2) B
# islice(data, 2, 4) C
# islice(data, 2, 4) D
# islice(data, 2, None) C
# islice(data, 2, None) D
# islice(data, 2, None) E
# islice(data, 2, None) F
# islice(data, 2, None) G
# islice(data, 2, None, 2) C
# islice(data, 2, None, 2) E
# islice(data, 2, None, 2) G

# islice_func()

def pairwise_func():
    data = 'ABCDEFG'
    a = itertools.pairwise(data)
    for ind in a:
        print(ind)
    # pairwise('ABCDEFG') → AB BC CD DE EF FG

# pairwise_func()

def permutations_func():
    # permutations('ABCD', 2) → AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) → 012 021 102 120 201 210
    data = "ABCD"
    a = itertools.permutations(data, 2)
    for ind in a:
        print("permutations(data, 2)", ind)

    data = range(3)
    a = itertools.permutations(data, 3)
    for ind in a:
        print("permutations(data, 3)", ind)

# permutations(data, 2) ('A', 'B')
# permutations(data, 2) ('A', 'C')
# permutations(data, 2) ('A', 'D')
# permutations(data, 2) ('B', 'A')
# permutations(data, 2) ('B', 'C')
# permutations(data, 2) ('B', 'D')
# permutations(data, 2) ('C', 'A')
# permutations(data, 2) ('C', 'B')
# permutations(data, 2) ('C', 'D')
# permutations(data, 2) ('D', 'A')
# permutations(data, 2) ('D', 'B')
# permutations(data, 2) ('D', 'C')
# permutations(data, 3) (0, 1, 2)
# permutations(data, 3) (0, 2, 1)
# permutations(data, 3) (1, 0, 2)
# permutations(data, 3) (1, 2, 0)
# permutations(data, 3) (2, 0, 1)
# permutations(data, 3) (2, 1, 0)

#permutations_func()

def product_func():
    data = "ABCD"
    data2 = 'xy'
    a = itertools.product(data, data2)
    for ind in a:
        print("product(data, repeat=repeat)=",ind)

    repeat=2
    a = itertools.product(data, data2, repeat=repeat)
    for ind in a:
        print("product(data, repeat=repeat, repeat=1)=",ind)

    repeat=3
    a = itertools.product(range(2), repeat=repeat)
    for ind in a:
        print("product(range(2), repeat=3)=",ind)
# product(data, repeat=repeat)= ('A', 'x')
# product(data, repeat=repeat)= ('A', 'y')
# product(data, repeat=repeat)= ('B', 'x')
# product(data, repeat=repeat)= ('B', 'y')
# product(data, repeat=repeat)= ('C', 'x')
# product(data, repeat=repeat)= ('C', 'y')
# product(data, repeat=repeat)= ('D', 'x')
# product(data, repeat=repeat)= ('D', 'y')
# product(data, repeat=repeat, repeat=1)= ('A', 'x', 'A', 'x')
# product(data, repeat=repeat, repeat=1)= ('A', 'x', 'A', 'y')
# product(data, repeat=repeat, repeat=1)= ('A', 'x', 'B', 'x')
# product(data, repeat=repeat, repeat=1)= ('A', 'x', 'B', 'y')
# product(data, repeat=repeat, repeat=1)= ('A', 'x', 'C', 'x')
# product(data, repeat=repeat, repeat=1)= ('A', 'x', 'C', 'y')
# product(data, repeat=repeat, repeat=1)= ('A', 'x', 'D', 'x')
# product(data, repeat=repeat, repeat=1)= ('A', 'x', 'D', 'y')
# product(data, repeat=repeat, repeat=1)= ('A', 'y', 'A', 'x')
# product(data, repeat=repeat, repeat=1)= ('A', 'y', 'A', 'y')
# product(data, repeat=repeat, repeat=1)= ('A', 'y', 'B', 'x')
# product(data, repeat=repeat, repeat=1)= ('A', 'y', 'B', 'y')
# product(data, repeat=repeat, repeat=1)= ('A', 'y', 'C', 'x')
# product(data, repeat=repeat, repeat=1)= ('A', 'y', 'C', 'y')
# product(data, repeat=repeat, repeat=1)= ('A', 'y', 'D', 'x')
# product(data, repeat=repeat, repeat=1)= ('A', 'y', 'D', 'y')
# product(data, repeat=repeat, repeat=1)= ('B', 'x', 'A', 'x')
# product(data, repeat=repeat, repeat=1)= ('B', 'x', 'A', 'y')
# product(data, repeat=repeat, repeat=1)= ('B', 'x', 'B', 'x')
# product(data, repeat=repeat, repeat=1)= ('B', 'x', 'B', 'y')
# product(data, repeat=repeat, repeat=1)= ('B', 'x', 'C', 'x')
# product(data, repeat=repeat, repeat=1)= ('B', 'x', 'C', 'y')
# product(data, repeat=repeat, repeat=1)= ('B', 'x', 'D', 'x')
# product(data, repeat=repeat, repeat=1)= ('B', 'x', 'D', 'y')
# product(data, repeat=repeat, repeat=1)= ('B', 'y', 'A', 'x')
# product(data, repeat=repeat, repeat=1)= ('B', 'y', 'A', 'y')
# product(data, repeat=repeat, repeat=1)= ('B', 'y', 'B', 'x')
# product(data, repeat=repeat, repeat=1)= ('B', 'y', 'B', 'y')
# product(data, repeat=repeat, repeat=1)= ('B', 'y', 'C', 'x')
# product(data, repeat=repeat, repeat=1)= ('B', 'y', 'C', 'y')
# product(data, repeat=repeat, repeat=1)= ('B', 'y', 'D', 'x')
# product(data, repeat=repeat, repeat=1)= ('B', 'y', 'D', 'y')
# product(data, repeat=repeat, repeat=1)= ('C', 'x', 'A', 'x')
# product(data, repeat=repeat, repeat=1)= ('C', 'x', 'A', 'y')
# product(data, repeat=repeat, repeat=1)= ('C', 'x', 'B', 'x')
# product(data, repeat=repeat, repeat=1)= ('C', 'x', 'B', 'y')
# product(data, repeat=repeat, repeat=1)= ('C', 'x', 'C', 'x')
# product(data, repeat=repeat, repeat=1)= ('C', 'x', 'C', 'y')
# product(data, repeat=repeat, repeat=1)= ('C', 'x', 'D', 'x')
# product(data, repeat=repeat, repeat=1)= ('C', 'x', 'D', 'y')
# product(data, repeat=repeat, repeat=1)= ('C', 'y', 'A', 'x')
# product(data, repeat=repeat, repeat=1)= ('C', 'y', 'A', 'y')
# product(data, repeat=repeat, repeat=1)= ('C', 'y', 'B', 'x')
# product(data, repeat=repeat, repeat=1)= ('C', 'y', 'B', 'y')
# product(data, repeat=repeat, repeat=1)= ('C', 'y', 'C', 'x')
# product(data, repeat=repeat, repeat=1)= ('C', 'y', 'C', 'y')
# product(data, repeat=repeat, repeat=1)= ('C', 'y', 'D', 'x')
# product(data, repeat=repeat, repeat=1)= ('C', 'y', 'D', 'y')
# product(data, repeat=repeat, repeat=1)= ('D', 'x', 'A', 'x')
# product(data, repeat=repeat, repeat=1)= ('D', 'x', 'A', 'y')
# product(data, repeat=repeat, repeat=1)= ('D', 'x', 'B', 'x')
# product(data, repeat=repeat, repeat=1)= ('D', 'x', 'B', 'y')
# product(data, repeat=repeat, repeat=1)= ('D', 'x', 'C', 'x')
# product(data, repeat=repeat, repeat=1)= ('D', 'x', 'C', 'y')
# product(data, repeat=repeat, repeat=1)= ('D', 'x', 'D', 'x')
# product(data, repeat=repeat, repeat=1)= ('D', 'x', 'D', 'y')
# product(data, repeat=repeat, repeat=1)= ('D', 'y', 'A', 'x')
# product(data, repeat=repeat, repeat=1)= ('D', 'y', 'A', 'y')
# product(data, repeat=repeat, repeat=1)= ('D', 'y', 'B', 'x')
# product(data, repeat=repeat, repeat=1)= ('D', 'y', 'B', 'y')
# product(data, repeat=repeat, repeat=1)= ('D', 'y', 'C', 'x')
# product(data, repeat=repeat, repeat=1)= ('D', 'y', 'C', 'y')
# product(data, repeat=repeat, repeat=1)= ('D', 'y', 'D', 'x')
# product(data, repeat=repeat, repeat=1)= ('D', 'y', 'D', 'y')
# product(range(2), repeat=3)= (0, 0, 0)
# product(range(2), repeat=3)= (0, 0, 1)
# product(range(2), repeat=3)= (0, 1, 0)
# product(range(2), repeat=3)= (0, 1, 1)
# product(range(2), repeat=3)= (1, 0, 0)
# product(range(2), repeat=3)= (1, 0, 1)
# product(range(2), repeat=3)= (1, 1, 0)
# product(range(2), repeat=3)= (1, 1, 1)

# product_func()

def repeat_func():
    data = 10
    times = 3
    a = itertools.repeat(data, times=times)
    for ind in a:
        print("repeat(10, times=10)=", ind)
# repeat(10, times=10)= 10
# repeat(10, times=10)= 10
# repeat(10, times=10)= 10

#repeat_func()

def starmap_func():
    data = [(2,5),(3,2),(10,3)]
    func = pow
    a = itertools.starmap(func, data)
    for ind in a:
        print(ind)
# 32
# 9
# 1000
# starmap_func()

def takewhile_func():
    predicate = lambda x: x< 5
    data = [1,4,6,3,8]
    a = itertools.takewhile(predicate, data)
    for ind in a:
        print(ind)

#takewhile_func()

def tee_func():
    data = "ABCD"
    n = 1
    [a] = itertools.tee(iter(data), n)
    for ind in [a]:
        for indind in ind:
            print(indind)
    # A
    # B
    # C
    # D
#tee_func()

def zip_longest_func():
    data = "ABCD"
    data2 = "xy"
    fillvalue="-"
    a = itertools.zip_longest(data, data2, fillvalue=fillvalue)
    for ind in a:
        print(ind)
# ('A', 'x')
# ('B', 'y')
# ('C', '-')
# ('D', '-')

zip_longest_func()



