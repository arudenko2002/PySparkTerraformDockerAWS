def max_result(arr):
    max_growth, cur_min, cur_min_idx = float('-inf'), float('inf'), -1
    res_l = res_h = float('-inf')
    for i, val in enumerate(arr):
        print(i, val,cur_min, val/cur_min)
        if val / cur_min > max_growth:
            max_growth = val / cur_min
            res_l, res_h = cur_min_idx, i
        if val < cur_min:
            cur_min, cur_min_idx = val, i
    return res_l + 1, res_h + 1, round(max_growth, 2)

arr = [10,5,2,8,3,10,4]
arr = [10,9, 8,6,5,4,3,2,1]
print(arr)
a,b,c = max_result(arr)
print("rez",a,b,c)
