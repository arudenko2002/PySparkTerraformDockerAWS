def maxWater_naive(arr):
    res = 0

    # For every element of the array
    for i in range(1, len(arr) - 1):

        # Find the maximum element on its left
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])

        # Find the maximum element on its right
        right = arr[i]
        for j in range(i + 1, len(arr)):
            right = max(right, arr[j])

        # Update the maximum water
        res += (min(left, right) - arr[i])

    return res

# Hpw it works
# for each i position we build pars of left max and right max
# we sum the rain min(left[i], right[i])-arr[i]

def maxWater(arr):
    n = len(arr)

    # Left array
    left = [0] * n
    # Right array
    right = [0] * n

    res = 0

    # Fill left array
    left[0] = arr[0]
    for i in range(1, n):
        print(i, left[i - 1], arr[i], max(left[i - 1], arr[i]))
        left[i] = max(left[i - 1], arr[i])
        print(i, left[i - 1], arr[i], max(left[i - 1], arr[i]))

    print("arr", arr)
    print("left",left)

    # Fill right array
    right[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], arr[i])
    print("right",right)

    # Calculate the accumulated water element by element
    for i in range(1, n - 1):
        min_of_2 = min(left[i], right[i])
        res += min_of_2 - arr[i]
        print(res, min_of_2, arr[i])

    return res


if __name__ == "__main__":
    arr = [2, 1, 5, 3, 1, 0, 4]
    print("max water=", maxWater(arr))
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    merged_dict = dict1 | dict2
    dict1.update(dict2)
    merged_dict = dict1
    merged_dict = {**dict1,**dict2}
    print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list1.extend(list2)
    print(list1)  # Output: [1, 2, 3, 4, 5, 6]

    list3 = [7, 8]
    list1.extend(list3)
    print(list1)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

    tuple1 = (9, 10)
    list1.extend(tuple1)
    print(list1)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]