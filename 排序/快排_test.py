def quicksort(arr, low, high):
    i = low
    j = high
    if i >= j:
        return arr
    temp = arr[low]
    while i<j:
        while i<j and arr[j] >= temp:
            j = j - 1
        a[i] = a[j]
        while i<j and arr[i] <= temp:
            i = i + 1
        a[j] = a[i]
    a[i] = temp
    print(arr)
    quicksort(arr, low, i-1)
    quicksort(arr, i+1, high)

a = [1,3,4,1,2,3,7,5]
quicksort(a, 0, len(a)-1)
print(a)
