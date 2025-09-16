def print_formatted(number):
    # your code goes here
    for num in range(number):
        num2 = num + 1
        l = len(str(bin(number))[2:])
        i = str(int(num2))
        o = str(oct(num2))[2:]
        h = str(hex(num2))[2:]
        b = str(bin(num2))[2:]
        ii = i.rjust(l)
        oo = o.rjust(l)
        hh = h.rjust(l).upper()
        bb = b.rjust(l)
        print(ii, oo, hh, bb)

if __name__ == '__main__':
    n = 99
    print_formatted(n)