import math
import os
import random
import re
import sys

#first_multiple_input = input().rstrip().split()

#n = int(first_multiple_input[0])
n = 7

#m = int(first_multiple_input[1])

m = 3

in_matrix  = """Tsi
h%x
i #
sM 
$a 
#t%
ir!
"""
m2=6
in_matrix2 = """#%$r%r
I%Mi$i
tiaxsp
#st%ct"""

m3=2
in_matrix3 = """# 
 @
"""
# matrix = []
#
# for _ in range(n):
#     matrix_item = input()
#     matrix.append(matrix_item)

def get_indexes(line, ch):
    return [pos for pos, char in enumerate(line) if char == ch]

matrix = in_matrix.split("\n")

coll = [""]*m
for ind in matrix:
    for ind2 in range(len(ind)):
        coll[ind2] += ind[ind2]

line = ""
for ind in coll:
    line += ind

coll = [""]*m
for ind in matrix:
    for ind2 in range(len(ind)):
        coll[ind2] += ind[ind2]

line = ""
for ind in coll:
    line += ind

reg = r"(?<=\w)([^\w\d]+)(?=\w)"
x = re.findall(reg, line)
print(5, reg, "X:", x)
print(6, re.findall(r"(?<=\w)",line))
print(7, re.findall(r"([^\w\d]+)",line))
print(8, re.findall(r"(?=\w)",line))
print(9, re.findall(r"(?=\w)([^\w\d]+)",line))
print(90, re.findall(r"([^\w\d]+)(?=\w)",line))
print(10,re.sub(reg, " ", line).strip())






