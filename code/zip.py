# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n = sys.stdin.readline()
ss = sys.stdin.readlines()
lines=[]
for line in ss:
    lines.append(list(map(float, line.split())))
ar = list(zip(*lines))
for array in ar:
    print(sum(array)/len(array))
