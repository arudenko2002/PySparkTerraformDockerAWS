# Function to find next smaller for every element
def nextSmaller(arr):
    n = len(arr)

    # Initialize with n for the cases when next smaller
    # does not exist
    nextS = [n] * n
    st = []

    # Traverse all array elements from left to right
    for i in range(n):
        print(st)
        while st and arr[i] < arr[st[-1]]:
            # Setting the index of the next smaller element
            # for the top of the stack
            ii = st.pop()
            print("ii=",ii)
            nextS[ii] = i
            print("nextS",nextS)
        st.append(i)

    return nextS


# Function to find previous smaller for every element
def prevSmaller(arr):
    n = len(arr)

    # Initialize with -1 for the cases when prev smaller
    # does not exist
    prevS = [-1] * n
    st = []

    # Traverse all array elements from left to right
    for i in range(n):
        while st and arr[i] < arr[st[-1]]:
            st.pop()
        if st:
            prevS[i] = st[-1]
        st.append(i)

    return prevS


# Function to calculate the maximum rectangular
# area in the Histogram
def getMaxArea(arr):
    prevS = prevSmaller(arr)
    nextS = nextSmaller(arr)
    maxArea = 0

    # Calculate the area for each arrogram bar
    for i in range(len(arr)):
        width = nextS[i] - prevS[i] - 1
        area = arr[i] * width
        maxArea = max(maxArea, area)

    return maxArea


if __name__ == "__main__":
    arr = [60, 20, 50, 40, 10, 50, 60]
    print(arr)
    print(getMaxArea(arr))

    from collections import defaultdict
    s = "Mamam myla  ramy"
    ss = s.split()
    d = defaultdict(int)
    print(ss)
    for word in ss:
        d[word] += 1
    print(d)
    print(d["abracadabra"])
