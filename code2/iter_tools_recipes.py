
def map_func():
    my_array = [1, 2, 3, 4, 5]

    # Using map()
    squared_array = list(map(lambda x: x**2, my_array))
    print(f"Squared array using map(): {squared_array}")

    # Using list comprehension
    cubed_array = [x**3 for x in my_array]
    print(f"Cubed array using list comprehension: {cubed_array}")
#map_func()
# Squared array using map(): [1, 4, 9, 16, 25]
# Cubed array using list comprehension: [1, 8, 27, 64, 125]

from collections import Counter, deque
from contextlib import suppress
from func_tools import reduce
from math import comb, prod, isqrt ,sumprod
from operator import itemgetter, getitem, mul, neg
import itertools

def take(n, iterable):
    "Return first n items of the iterable as a list."
    return list(itertools.islice(iterable, n))

data = [1,2,3,4,5]
# print("take(3, data)=", take(3, data))
# take(3, data): [1, 2, 3]

def prepend(value, iterable):
    "Prepend a single value in front of an iterable."
    # prepend(1, [2, 3, 4]) → 1 2 3 4
    return itertools.chain([value], iterable)

data = [2,3,4]
prep = 1
a = prepend(prep, data)
# for ind in a:
#     print("prepend(1, data)=", ind)
# prepend(1, data)= 1
# prepend(1, data)= 2
# prepend(1, data)= 3
# prepend(1, data)= 4


def tabulate(function, start=0):
    "Return function(0), function(1), ..."
    return map(function, itertools.count(start))

start = 10
a = tabulate(lambda x: 2*x, start=start)
b = itertools.count(start)
# for ind in b:
#     print(ind)
#     if ind==15:
#         break
# 10
# 11
# 12
# 13
# 14
# 15

# for ind in a:
#     if ind <= 30:
#         print("tabulate(lambda x: 2*x, start=10)=", ind)

# tabulate(lambda x: 2*x, start=10)= 20
# tabulate(lambda x: 2*x, start=10)= 22
# tabulate(lambda x: 2*x, start=10)= 24
# tabulate(lambda x: 2*x, start=10)= 26
# tabulate(lambda x: 2*x, start=10)= 28
# tabulate(lambda x: 2*x, start=10)= 30

def repeatfunc(function, times=None, *args):
    "Repeat calls to a function with specified arguments."
    if times is None:
        return itertools.starmap(function, itertools.repeat(args))
    return itertools.starmap(function, itertools.repeat(args, times))

a = repeatfunc(lambda x: x*3, 5, [1,2,3])
# for ind in a:
#     print("repeatfunc(lambda x: x*3, 5, [1,2,3])=", ind)
# repeatfunc(lambda x: x*3, 5, [1,2,3])= [1, 2, 3, 1, 2, 3, 1, 2, 3]
# repeatfunc(lambda x: x*3, 5, [1,2,3])= [1, 2, 3, 1, 2, 3, 1, 2, 3]
# repeatfunc(lambda x: x*3, 5, [1,2,3])= [1, 2, 3, 1, 2, 3, 1, 2, 3]
# repeatfunc(lambda x: x*3, 5, [1,2,3])= [1, 2, 3, 1, 2, 3, 1, 2, 3]
# repeatfunc(lambda x: x*3, 5, [1,2,3])= [1, 2, 3, 1, 2, 3, 1, 2, 3]

def flatten(list_of_lists):
    "Flatten one level of nesting."
    return itertools.chain.from_iterable(list_of_lists)

a = flatten([[1,2,3],[10,11,12],[20,21,22]])
# for ind in a:
#     print("flatten([[1,2,3],[10,11,12],[20,21,22]])=", ind)
# flatten([[1,2,3],[10,11,12],[20,21,22]])= 1
# flatten([[1,2,3],[10,11,12],[20,21,22]])= 2
# flatten([[1,2,3],[10,11,12],[20,21,22]])= 3
# flatten([[1,2,3],[10,11,12],[20,21,22]])= 10
# flatten([[1,2,3],[10,11,12],[20,21,22]])= 11
# flatten([[1,2,3],[10,11,12],[20,21,22]])= 12
# flatten([[1,2,3],[10,11,12],[20,21,22]])= 20
# flatten([[1,2,3],[10,11,12],[20,21,22]])= 21
# flatten([[1,2,3],[10,11,12],[20,21,22]])= 22

def ncycles(iterable, n):
    "Returns the sequence elements n times."
    return itertools.chain.from_iterable(itertools.repeat(tuple(iterable), n))

a= ncycles([1,2,3], 3)

# for ind in a:
#     print("ncycles([1,2,3], 3)=", ind)
# ncycles([1,2,3], 3)= 1
# ncycles([1,2,3], 3)= 2
# ncycles([1,2,3], 3)= 3
# ncycles([1,2,3], 3)= 1
# ncycles([1,2,3], 3)= 2
# ncycles([1,2,3], 3)= 3
# ncycles([1,2,3], 3)= 1
# ncycles([1,2,3], 3)= 2
# ncycles([1,2,3], 3)= 3

def loops(n):
    "Loop n times. Like range(n) but without creating integers."
    # for _ in loops(100): ...
    return itertools.repeat(None, n)

a = loops(10)
# for num,ind in enumerate(a):
#     print(num,"loops(10)=",ind)
# 0 loops(10)= None
# 1 loops(10)= None
# 2 loops(10)= None
# 3 loops(10)= None
# 4 loops(10)= None
# 5 loops(10)= None
# 6 loops(10)= None
# 7 loops(10)= None
# 8 loops(10)= None
# 9 loops(10)= None

def tail(n, iterable):
    "Return an iterator over the last n items."
    # tail(3, 'ABCDEFG') → E F G
    return iter(deque(iterable, maxlen=n))

a = tail(3,[1,2,3,4,5,6,7,8,9])
# for ind in a:
#     print("tail(3,[1,2,3,4,5,6,7,8,9])=", ind)
# tail(3,[1,2,3,4,5,6,7,8,9])= 7
# tail(3,[1,2,3,4,5,6,7,8,9])= 8
# tail(3,[1,2,3,4,5,6,7,8,9])= 9

def consume(iterator, n=None):
    "Advance the iterator n-steps ahead. If n is None, consume entirely."
    # Use functions that consume iterators at C speed.
    if n is None:
        return deque(iterator, maxlen=0)
    else:
        return next(itertools.islice(iterator, n-1, n), None)


# data = [1,2,3,4,5,6,7,8,9]
# a = consume( data, n=9)
# print(a)

def nth(iterable, n, default=None):
    "Returns the nth item or a default value."
    return next(itertools.islice(iterable, n, None), default)

a = nth([1,2,3,4,5,6,7,8,9], 3)
# print("nth([1,2,3,4,5,6,7,8,9], 3)=", a)
# nth([1,2,3,4,5,6,7,8,9], 3)= 4

def quantify(iterable, predicate=bool):
    "Given a predicate that returns True or False, count the True results."
    return sum(map(predicate, iterable))

predicate=lambda x: x%2==0
a = quantify([1,2,3,4,5,6,7,8,9], predicate=predicate)
# print("count all evens in [1,2,3,4,5,6,7,8,9], predicate=lambda x: x%2==0)=", a)
# count all evens in [1,2,3,4,5,6,7,8,9], predicate=lambda x: x%2==0)= 4

def first_true(iterable, default=False, predicate=None):
    "Returns the first true value or the *default* if there is no true value."
    # first_true([a,b,c], x) → a or b or c or x
    # first_true([a,b], x, f) → a if f(a) else b if f(b) else x
    return next(filter(predicate, iterable), default)

a = first_true([1,2,3,4,5,6,7,8,9], predicate=predicate)
#print("first_true([1,2,3,4,5,6,7,8,9], predicate=predicate)=", a)
#first_true([1,2,3,4,5,6,7,8,9], predicate=predicate)= 2


def all_equal(iterable, key=None):
    "Returns True if all the elements are equal to each other."
    # all_equal('4٤௪౪໔', key=int) → True
    return len(take(2, itertools.groupby(iterable, key))) <= 1

# a = all_equal([1,1,1,1,1,1,1,1,1,1,1], key=None)
# print(a)
# a = all_equal([1,1,1,1,1,2,1,1,1,1,1], key=None)
# print(a)
# True
# False

def unique_justseen(iterable, key=None):
    "Yield unique elements, preserving order. Remember only the element just seen."
    # unique_justseen('AAAABBBCCDAABBB') → A B C D A B
    # unique_justseen('ABBcCAD', str.casefold) → A B c A D
    if key is None:
        return map(itemgetter(0), itertools.groupby(iterable))
    return map(next, map(itemgetter(1), itertools.groupby(iterable, key)))

a = unique_justseen("AAABBBCCCCaAABBB", key=str.casefold)
# for ind in a:
#     print(ind)
# print("no key:")
# a = unique_justseen("AAABBBCCCCaAABBB")
# for ind in a:
#     print(ind)
# A
# B
# C
# a
# B
# no key:
# A
# B
# C
# a
# A
# B

def unique_everseen(iterable, key=None):
    "Yield unique elements, preserving order. Remember all elements ever seen."
    # unique_everseen('AAAABBBCCDAABBB') → A B C D
    # unique_everseen('ABBcCAD', str.casefold) → A B c D
    seen = set()
    if key is None:
        for element in itertools.filterfalse(seen.__contains__, iterable):
            seen.add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen.add(k)
                yield element

a = unique_everseen("AAABBBCCCCaAABBB", key=str.casefold)
# for ind in a:
#     print(ind)
# print("no key:")
# a = unique_everseen("AAABBBCCCCaAABBB")
# for ind in a:
#     print(ind)

# A
# B
# C
# no key:
# A
# B
# C
# a

def unique(iterable, key=None, reverse=False):
   "Yield unique elements in sorted order. Supports unhashable inputs."
   # unique([[1, 2], [3, 4], [1, 2]]) → [1, 2] [3, 4]
   sequenced = sorted(iterable, key=key, reverse=reverse)
   return unique_justseen(sequenced, key=key)

a = unique([[1, 2], [3, 4], [1, 2]])
# for ind in a:
#     print("unique([[1, 2], [3, 4], [1, 2]]) =", ind)
# unique([[1, 2], [3, 4], [1, 2]]) = [1, 2]
# unique([[1, 2], [3, 4], [1, 2]]) = [3, 4]

def sliding_window(iterable, n):
    "Collect data into overlapping fixed-length chunks or blocks."
    # sliding_window('ABCDEFG', 4) → ABCD BCDE CDEF DEFG
    iterator = iter(iterable)
    window = deque(itertools.islice(iterator, n - 1), maxlen=n)
    for x in iterator:
        window.append(x)
        yield tuple(window)

a = sliding_window([1,2,3,4,5,6,7,8,9], 3)
# for ind in a:
#     print("sliding_window([1,2,3,4,5,6,7,8,9], 3) = ", ind)
# sliding_window([1,2,3,4,5,6,7,8,9], 3) =  (1, 2, 3)
# sliding_window([1,2,3,4,5,6,7,8,9], 3) =  (2, 3, 4)
# sliding_window([1,2,3,4,5,6,7,8,9], 3) =  (3, 4, 5)
# sliding_window([1,2,3,4,5,6,7,8,9], 3) =  (4, 5, 6)
# sliding_window([1,2,3,4,5,6,7,8,9], 3) =  (5, 6, 7)
# sliding_window([1,2,3,4,5,6,7,8,9], 3) =  (6, 7, 8)
# sliding_window([1,2,3,4,5,6,7,8,9], 3) =  (7, 8, 9)

def grouper(iterable, n, *, incomplete='fill', fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks."
    # grouper('ABCDEFG', 3, fillvalue='x') → ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') → ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') → ABC DEF
    iterators = [iter(iterable)] * n
    match incomplete:
        case 'fill':
            return itertools.zip_longest(*iterators, fillvalue=fillvalue)
        case 'strict':
            return zip(*iterators, strict=True)
        case 'ignore':
            return zip(*iterators)
        case _:
            raise ValueError('Expected fill, strict, or ignore')

# a = grouper('ABCDEFG', 3, fillvalue='x')
# for ind in a:
#     print("grouper('ABCDEFG', 3, fillvalue='x') =", ind)
# a = grouper('ABCDEFG', 3, incomplete='strict')
# try:
#     for ind in a:
#         print("grouper('ABCDEFG', 3, incomplete='strict') =", ind)
# except Exception as e:
#     print("grouper('ABCDEFG', 3, incomplete='strict') =", "Error",e)
#
# a = grouper('ABCDEFG', 3, incomplete='ignore')
# for ind in a:
#     print("grouper('ABCDEFG', 3, incomplete='ignore') =", ind)
# grouper('ABCDEFG', 3, fillvalue='x') = ('A', 'B', 'C')
# grouper('ABCDEFG', 3, fillvalue='x') = ('D', 'E', 'F')
# grouper('ABCDEFG', 3, fillvalue='x') = ('G', 'x', 'x')
# grouper('ABCDEFG', 3, incomplete='strict') = ('A', 'B', 'C')
# grouper('ABCDEFG', 3, incomplete='strict') = ('D', 'E', 'F')
# grouper('ABCDEFG', 3, incomplete='strict') = Error zip() argument 2 is shorter than argument 1
# grouper('ABCDEFG', 3, incomplete='ignore') = ('A', 'B', 'C')
# grouper('ABCDEFG', 3, incomplete='ignore') = ('D', 'E', 'F')


def roundrobin(*iterables):
    "Visit input iterables in a cycle until each is exhausted."
    # roundrobin('ABC', 'D', 'EF') → A D E B F C
    # Algorithm credited to George Sakkis
    iterators = map(iter, iterables)
    for num_active in range(len(iterables), 0, -1):
        iterators = itertools.cycle(itertools.islice(iterators, num_active))
        yield from map(next, iterators)

a = roundrobin('ABC', 'D', 'EF')
# for ind in a:
#     print("roundrobin('ABC', 'D', 'EF') =", ind)
# roundrobin('ABC', 'D', 'EF') = A
# roundrobin('ABC', 'D', 'EF') = D
# roundrobin('ABC', 'D', 'EF') = E
# roundrobin('ABC', 'D', 'EF') = B
# roundrobin('ABC', 'D', 'EF') = F
# roundrobin('ABC', 'D', 'EF') = C

def subslices(seq):
    "Return all contiguous non-empty subslices of a sequence."
    # subslices('ABCD') → A AB ABC ABCD B BC BCD C CD D
    slices = itertools.starmap(slice, itertools.combinations(range(len(seq) + 1), 2))
    return map(getitem, itertools.repeat(seq), slices)

a = subslices('ABCD')
# for ind in a:
#     print(ind)
# A
# AB
# ABC
# ABCD
# B
# BC
# BCD
# C
# CD
# D

def iter_index(iterable, value, start=0, stop=None):
    "Return indices where a value occurs in a sequence or iterable."
    # iter_index('AABCADEAF', 'A') → 0 1 4 7
    seq_index = getattr(iterable, 'index', None)
    if seq_index is None:
        iterator = itertools.islice(iterable, start, stop)
        for i, element in enumerate(iterator, start):
            if element is value or element == value:
                yield i
    else:
        stop = len(iterable) if stop is None else stop
        i = start
        with suppress(ValueError):
            while True:
                yield (i := seq_index(value, i, stop))
                i += 1

a = iter_index('AABCADEAF', 'A')
# for ind in a:
#     print("iter_index('AABCADEAF', 'A') =", ind)
# iter_index('AABCADEAF', 'A') = 0
# iter_index('AABCADEAF', 'A') = 1
# iter_index('AABCADEAF', 'A') = 4
# iter_index('AABCADEAF', 'A') = 7

def iter_except(function, exception, first=None):
    "Convert a call-until-exception interface to an iterator interface."
    # iter_except(d.popitem, KeyError) → non-blocking dictionary iterator
    with suppress(exception):
        if first is not None:
            yield first()
        while True:
            yield function()

data = {'a':'b', 'c':'d', 'e':'f'}
a = iter_except(data.popitem, KeyError)
# for ind in a:
#     print('iter_except(data.popitem, KeyError) =', ind)
# iter_except(data.popitem, KeyError) = ('e', 'f')
# iter_except(data.popitem, KeyError) = ('c', 'd')
# iter_except(data.popitem, KeyError) = ('a', 'b')

# The following recipes have a more mathematical flavor:

def powerset(iterable):
    "Subsequences of the iterable from shortest to longest."
    # powerset([1,2,3]) → () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

a = powerset([1,2,3])
# for ind in a:
#     print(ind)
# ()
# (1,)
# (2,)
# (3,)
# (1, 2)
# (1, 3)
# (2, 3)
# (1, 2, 3)

# not working
def sum_of_squares(iterable):
    "Add up the squares of the input values."
    # sum_of_squares([10, 20, 30]) → 1400
    return sumprod(*itertools.tee(iterable))
a = sum_of_squares([10,20,30])
# print("sum_of_squares([10,20,30]) =", a)


def reshape(matrix, columns):
    "Reshape a 2-D matrix to have a given number of columns."
    # reshape([(0, 1), (2, 3), (4, 5)], 3) →  (0, 1, 2), (3, 4, 5)
    return itertools.batched(itertools.chain.from_iterable(matrix), columns, strict=True)

a = reshape([(0, 1), (2, 3), (4, 5)], 3)
# for ind in a:
#     print("reshape([(0, 1), (2, 3), (4, 5)], 3) =", ind)
# reshape([(0, 1), (2, 3), (4, 5)], 3) = (0, 1, 2)
# reshape([(0, 1), (2, 3), (4, 5)], 3) = (3, 4, 5)

def transpose(matrix):
    "Swap the rows and columns of a 2-D matrix."
    # transpose([(1, 2, 3), (11, 22, 33)]) → (1, 11) (2, 22) (3, 33)
    return zip(*matrix) #, strict=True)

a = transpose([(1, 2, 3), (11, 22, 33)])
# for ind in a:
#     print("transpose([(1, 2, 3), (11, 22, 33)]) =", ind)
# transpose([(1, 2, 3), (11, 22, 33)]) = (1, 11)
# transpose([(1, 2, 3), (11, 22, 33)]) = (2, 22)
# transpose([(1, 2, 3), (11, 22, 33)]) = (3, 33)

def matmul(m1, m2):
    "Multiply two matrices."
    # matmul([(7, 5), (3, 5)], [(2, 5), (7, 9)]) → (49, 80), (41, 60)
    n = len(m2[0])
    return itertools.batched(itertools.starmap(sumprod, itertools.product(m1, transpose(m2))), n)

a = matmul([(7, 5), (3, 5)], [(2, 5), (7, 9)])
# for ind in a:
#     print("matmul([(7, 5), (3, 5)], [(2, 5), (7, 9)])", ind)
# matmul([(7, 5), (3, 5)], [(2, 5), (7, 9)]) (49, 80)
# matmul([(7, 5), (3, 5)], [(2, 5), (7, 9)]) (41, 60)

# sumrod not working
def convolve(signal, kernel):
    """Discrete linear convolution of two iterables.
    Equivalent to polynomial multiplication.

    Convolutions are mathematically commutative; however, the inputs are
    evaluated differently.  The signal is consumed lazily and can be
    infinite. The kernel is fully consumed before the calculations begin.

    Article:  https://betterexplained.com/articles/intuitive-convolution/
    Video:    https://www.youtube.com/watch?v=KuXjwB4LzSA
    """
    # convolve([1, -1, -20], [1, -3]) → 1 -4 -17 60
    # convolve(data, [0.25, 0.25, 0.25, 0.25]) → Moving average (blur)
    # convolve(data, [1/2, 0, -1/2]) → 1st derivative estimate
    # convolve(data, [1, -2, 1]) → 2nd derivative estimate
    kernel = tuple(kernel)[::-1]
    n = len(kernel)
    padded_signal = itertools.chain(itertools.repeat(0, n-1), signal, itertools.repeat(0, n-1))
    windowed_signal = sliding_window(padded_signal, n)
    return map(sumprod, itertools.repeat(kernel), windowed_signal)

a = convolve([1, -1, -20], [1, -3])
# for ind in a:
#     print("convolve([1, -1, -20], [1, -3]) =", ind)
#
# a = convolve([1, -1, -20], [0.25, 0.25, 0.25, 0.25])
# for ind in a:
#     print("convolve([1, -1, -20], [0.25, 0.25, 0.25, 0.25]) =", ind)
#
# a = convolve([1, -1, -20], [1/2, 0, -1/2])
# for ind in a:
#     print("convolve([1, -1, -20], [1/2, 0, -1/2]) =", ind)
#
# a = convolve([1, -1, -20], [1, -2, 1])
# for ind in a:
#     print("convolve([1, -1, -20], [1, -2, 1]) =", ind)
# convolve([1, -1, -20], [1, -3]) = 1
# convolve([1, -1, -20], [1, -3]) = -4
# convolve([1, -1, -20], [1, -3]) = -17
# convolve([1, -1, -20], [1, -3]) = 60
# convolve([1, -1, -20], [0.25, 0.25, 0.25, 0.25]) = 0.25
# convolve([1, -1, -20], [0.25, 0.25, 0.25, 0.25]) = 0.0
# convolve([1, -1, -20], [0.25, 0.25, 0.25, 0.25]) = -5.0
# convolve([1, -1, -20], [0.25, 0.25, 0.25, 0.25]) = -5.0
# convolve([1, -1, -20], [0.25, 0.25, 0.25, 0.25]) = -5.25
# convolve([1, -1, -20], [0.25, 0.25, 0.25, 0.25]) = -5.0
# convolve([1, -1, -20], [1/2, 0, -1/2]) = 0.5
# convolve([1, -1, -20], [1/2, 0, -1/2]) = -0.5
# convolve([1, -1, -20], [1/2, 0, -1/2]) = -10.5
# convolve([1, -1, -20], [1/2, 0, -1/2]) = 0.5
# convolve([1, -1, -20], [1/2, 0, -1/2]) = 10.0
# convolve([1, -1, -20], [1, -2, 1]) = 1
# convolve([1, -1, -20], [1, -2, 1]) = -3
# convolve([1, -1, -20], [1, -2, 1]) = -17
# convolve([1, -1, -20], [1, -2, 1]) = 39
# convolve([1, -1, -20], [1, -2, 1]) = -20
def polynomial_from_roots(roots):
    """Compute a polynomial's coefficients from its roots.

       (x - 5) (x + 4) (x - 3)  expands to:   x³ -4x² -17x + 60
    """
    # polynomial_from_roots([5, -4, 3]) → [1, -4, -17, 60]
    factors = zip(itertools.repeat(1), map(neg, roots))
    return list(reduce(convolve, factors, [1]))

a = polynomial_from_roots([5, -4, 3])
# for ind in a:
#     print("polynomial_from_roots([5, -4, 3]) =", ind)
# polynomial_from_roots([5, -4, 3]) = 1
# polynomial_from_roots([5, -4, 3]) = -4
# polynomial_from_roots([5, -4, 3]) = -17
# polynomial_from_roots([5, -4, 3]) = 60

def polynomial_eval(coefficients, x):
    """Evaluate a polynomial at a specific value.

    Computes with better numeric stability than Horner's method.
    """
    # Evaluate x³ -4x² -17x + 60 at x = 5
    # polynomial_eval([1, -4, -17, 60], x=5) → 0
    n = len(coefficients)
    if not n:
        return type(x)(0)
    powers = map(pow, itertools.repeat(x), reversed(range(n)))
    return sumprod(coefficients, powers)

a = polynomial_eval([1, -4, -17, 60], x=5)
print("polynomial_eval([1, -4, -17, 60], x=5)", a)
# polynomial_eval([1, -4, -17, 60], x=5) 0

def polynomial_derivative(coefficients):
    """Compute the first derivative of a polynomial.

       f(x)  =  x³ -4x² -17x + 60
       f'(x) = 3x² -8x  -17
    """
    # polynomial_derivative([1, -4, -17, 60]) → [3, -8, -17]
    n = len(coefficients)
    powers = reversed(range(1, n))
    return list(map(mul, coefficients, powers))

a = polynomial_derivative([1, -4, -17, 60])
# for ind in a:
#     print("polynomial_derivative([1, -4, -17, 60]) =", ind)
# polynomial_derivative([1, -4, -17, 60]) = 3
# polynomial_derivative([1, -4, -17, 60]) = -8
# polynomial_derivative([1, -4, -17, 60]) = -17

def sieve(n):
    "Primes less than n."
    # sieve(30) → 2 3 5 7 11 13 17 19 23 29
    if n > 2:
        yield 2
    data = bytearray((0, 1)) * (n // 2)
    for p in iter_index(data, 1, start=3, stop=isqrt(n) + 1):
        data[p*p : n : p+p] = bytes(len(range(p*p, n, p+p)))
    yield from iter_index(data, 1, start=3)

a = sieve(30)
# for ind in a:
#     print("sieve(30) =", ind)
# sieve(30) = 2
# sieve(30) = 3
# sieve(30) = 5
# sieve(30) = 7
# sieve(30) = 11
# sieve(30) = 13
# sieve(30) = 17
# sieve(30) = 19
# sieve(30) = 23
# sieve(30) = 29

def factor(n):
    "Prime factors of n."
    # factor(99) → 3 3 11
    # factor(1_000_000_000_000_007) → 47 59 360620266859
    # factor(1_000_000_000_000_403) → 1000000000000403
    for prime in sieve(isqrt(n) + 1):
        while not n % prime:
            yield prime
            n //= prime
            if n == 1:
                return
    if n > 1:
        yield n

a = factor(99)
# for ind in a:
#     print("factor(99) =", ind)
# factor(99) = 3
# factor(99) = 3
# factor(99) = 11

def is_prime(n):
    "Return True if n is prime."
    # is_prime(1_000_000_000_000_403) → True
    return n > 1 and next(factor(n)) == n

a = is_prime(1_000_000_000_000_403)
# print("is_prime(1_000_000_000_000_403) =", a)
# is_prime(1_000_000_000_000_403) = True

def totient(n):
    "Count of natural numbers up to n that are coprime to n."
    # https://mathworld.wolfram.com/TotientFunction.html
    # totient(12) → 4 because len([1, 5, 7, 11]) == 4
    for prime in set(factor(n)):
        n -= n // prime
    return n

a = totient(12)
# print("totient(12) =", a)
# totient(12) = 4

def multinomial(*counts):
    "Number of distinct arrangements of a multiset."
    # Counter('abracadabra').values() -> 5 2 1 1 2
    # multinomial(5, 2, 1, 1, 2) → 83160
    return prod(map(comb, itertools.accumulate(counts), counts))

a = multinomial(5, 2, 1, 1, 2)
# print("multinomial(5, 2, 1, 1, 2) =", a)
# multinomial(5, 2, 1, 1, 2) = 83160
