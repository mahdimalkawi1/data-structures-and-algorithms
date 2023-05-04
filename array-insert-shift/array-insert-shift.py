def insertShiftArray(arr, val):
    n = len(arr)
    mid = n // 2
    if n % 2 == 1:
        for i in range(mid+1, n):
            arr[i], val = val, arr[i]
        arr.append(val)
    else:
        for i in range(mid, n):
            arr[i], val = val, arr[i]
        arr.append(val)
    return arr
print(insertShiftArray([5,8,7,9,10],15))
