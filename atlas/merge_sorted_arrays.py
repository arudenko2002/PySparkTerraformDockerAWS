def merge_arrays(ar1, ar2):
    i=0
    j=0
    ar3=[]
    while True:
        if i==len(ar1) or j==len(ar2):
            break
        if ar1[i]>ar2[j]:
            ar3.append(ar2[j])
            j += 1
        else:
            ar3.append(ar1[i])
            i += 1

    print(i, j)
    if i<=len(ar1)-1:
        ar3 += ar1[i:]

    if j<=len(ar2)-1:
        ar3 += ar2[j:]
    return ar3





ar1 = [1, 3, 5, 7]
ar2 = [2, 4, 6, 8]
ar3 = merge_arrays(ar1, ar2)

print(" ".join(map(str, ar3)))