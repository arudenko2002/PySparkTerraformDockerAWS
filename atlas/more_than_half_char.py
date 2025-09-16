
def majorityElement():
    arr = [4,4,4,6,6,6,6,6,6,6,6,6,3]
    print(len(arr))
    n = len(arr)
    candidate = -1
    count = 0

    # Find a candidate
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
        print(num, count)

    print(candidate, count)
    # Validate the candidate
    count = 0
    for num in arr:
        if num == candidate:
            count += 1

        # If count is greater than n / 2, return the candidate; otherwise, return -1
    if count > n // 2:
        return candidate, count
    else:
        return -1, -1

print("candidate, count=", majorityElement())