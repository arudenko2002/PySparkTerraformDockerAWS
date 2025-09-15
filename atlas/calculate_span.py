def calculateSpan(arr):
    print(arr)
    n = len(arr)
    span = [0]*n
    stk = []

    for i in range(n):
        while stk and arr[stk[-1]] <= arr[i]:
            stk.pop()

        if not stk:
            span[i] = (i+1)
        else:
            span[i] = (i - stk[-1])

        stk.append(i)
        print(stk)
        print("stk=", stk[-1])
    return span

arr = [10, 4, 5, 90, 120, 80]
span = calculateSpan(arr)
for x in span:
    print(x, end=" ")


