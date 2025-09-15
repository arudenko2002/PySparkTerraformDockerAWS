if __name__ == '__main__':
    x = 1 #int(input())
    y = 1 #int(input())
    z = 1 #int(input())
    n = 2 #int(input())
    rez = []
    for ix in range(x+1):
        for iy in range(y+1):
            for iz in range(z+1):
                if ix +iy+iz != n:
                    rez.append([ix,iy,iz])
    print(rez)
    """
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
    """

# runner-up score
if __name__ == '__main__':
    n = 5 #int(input())
    arr = [2,3,6,6,5] # map(int, input().split())

    arr2 = sorted(arr, reverse=True)
    for ind in range(len(arr2)):
        if arr2[ind] < arr2[0]:
            print(arr2[ind])
            break
    """
    5
    """

# prin a student with second least score
if __name__ == '__main__':
    arr = []
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     arr.append([name, score])
    arr = [["Harry", 37.21], ["Berry",37.21],["Tina",37.2],["Akriti",41],["Harsh",39]]

    arr2 = sorted(arr, key=lambda x: x[1])
    second = 0.0
    for ind in arr2:
        if ind[1] > arr2[0][1]:
            second = ind[1]
            break

    rez = []
    for ind in arr2:
        if ind[1] == second:
            rez.append(ind[0])

    r = sorted(rez)
    for ind in r:
        print(ind)
    """
        Berry
        Harry
    """

# find average
if __name__ == '__main__':
    n = 3 #int(input())
    # student_marks = {}
    # for _ in range(n):
    #     name, *line = input().split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    student_marks = {
        "Krishna": [67,68,69],
        "Arjun": [70,98,63],
        "Malika": [52,56,60]}
    query_name = "Malika" #input()
    avg  = sum(student_marks[query_name])/len(student_marks[query_name])
    print(f"{avg:.2f}")
    """
    56.00
    """

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
numpy.set_printoptions(legacy='1.13')

ss = "1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9" #input()
arr = [float(x) for x in ss.split()]
my_arr = numpy.array(arr)
print("floor", numpy.floor(my_arr))
print("ceil", numpy.ceil(my_arr))
print("rint", numpy.rint(my_arr))
"""
floor [ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
ceil [  2.   3.   4.   5.   6.   7.   8.   9.  10.]
rint [  1.   2.   3.   4.   6.   7.   8.   9.  10.]
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
s = ["1","1"] #input().split()
n = 2 #int(s[0])
m = 2 #int(s[1])
# arr = []
# for ind in range(n):
#     s = input().split()
#     numbers = list(map(int, s))
#     arr.append(numbers)

arr = [[1,2],[3,4]]

my_array = numpy.array(arr)
my_array_sum = numpy.sum(my_array, axis=0)
my_array_sum_prod = numpy.prod(my_array_sum)
print(my_array_sum_prod)
"""
24
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
# s = input().split()
# n = int(s[0])
# m = int(s[1])
# arr = []
# for ind in range(n):
#     s = input().split()
#     numbers = list(map(int, s))
#     arr.append(numbers)
arr = [[2, 5], [3,7], [1, 3], [4,0]]

my_array = numpy.array(arr)
my_array_min = numpy.min(my_array, axis=1)
my_arra_min_max = numpy.max(my_array_min)
print(my_arra_min_max)
"""
3
"""

# s = input().split()
# n = int(s[0])
# m = int(s[1])
# arr = []
# for ind in range(n):
#     s = input().split()
#     numbers = list(map(int, s))
#     arr.append(numbers)
arr = [[1,2],[3,4]]

my_array = numpy.array(arr)
print(numpy.mean(my_array, axis=1))
print(numpy.var(my_array, axis=0))
print(round(numpy.std(my_array, axis=None), 11))
"""
[ 1.5  3.5]
[ 1.  1.]
1.11803398875
"""

# Multiplication of Matrixes
# Enter your code here. Read input from STDIN. Print output to STDOUT
# s = input()
# n = int(s)
# arr1 = []
# for ind in range(n):
#     s = input().split()
#     numbers = list(map(int, s))
#     arr1.append(numbers)
# arr2 = []
# for ind in range(n):
#     s = input().split()
#     numbers = list(map(int, s))
#     arr2.append(numbers)
arr1 = [[1,2],[3,4]]
arr2 = [[1,2],[3,4]]

arr3 = numpy.matmul(arr1, arr2)
print(arr3)
"""
[[ 7 10]
 [15 22]]
"""

# Multiplication of arrays
# s = input().split()
# arr1 = list(map(int, s))
# s = input().split()
# arr2 = list(map(int, s))

arr1 = [0,1] # numpy.array(arr1)
arr2 = [3,4] #numpy.array(arr2)

print(numpy.inner(arr1,arr2))
print(numpy.outer(arr1,arr2))
"""
4
[[0 0]
 [3 4]]
"""


