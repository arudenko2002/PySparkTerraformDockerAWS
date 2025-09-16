#extract subarray with max sum--
arr = [-100,1,2,3,4,-2, 11, -100, 1,2,3,4,5,6,7,8,9]
arr = [-100,1,2,3,4,-2, 11, -100]
arr = [-100,1,2,3,4,-48, 9]

def find_max_subarray(arr):
    msum = 0
    mi = 0
    mj = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            # print(i, j, msum)
            ssum = sum(arr[i:j+1])
            if ssum>=msum:
                msum = ssum
                mi = i
                mj = j

    return [mi, mj], msum

print(find_max_subarray(arr))