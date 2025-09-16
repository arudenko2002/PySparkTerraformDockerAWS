import numpy

# Enter your code here. Read input from STDIN. Print output to STDOUT
# nm = input().split()
# n = int(nm[0])
# m = int(nm[1])
# aa = []
# bb = []
# for ind in range(n):
#     aa.append(list(map(int, input().split())))
# for ind in range(n):
#     bb.append(list(map(int, input().split())))
n = 1
m = 4
aa = [[1, 2, 3, 4]]
bb = [[5, 6, 7, 8]]

n = 2
m = 4
aa = [[1, 2, 3, 4], [1, 2, 3, 4]]
bb = [[5, 6, 7, 7],[5, 6, 7, 7]]

a = numpy.array(aa, int)
b = numpy.array(bb, int)
print("a",a)
print("b",b)
print("add",numpy.add(a, b))
print("subtract",numpy.subtract(a, b))
print("multiply",numpy.multiply(a, b))
print("divide", numpy.divide(a, b).astype(int))
print("mod",numpy.mod(a, b))
print("power",numpy.power(a, b))