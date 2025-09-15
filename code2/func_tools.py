from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x,y:x*y, fracs) # complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    input_array = ["1 2","3 4","10 6"]
    # for _ in range(int(input())):
    #     fracs.append(Fraction(*map(int, input().split())))
    for ind in range(len(input_array)):
        fracs.append(Fraction(*map(int, input_array[ind].split())))
    result = product(fracs)
    print(*result)