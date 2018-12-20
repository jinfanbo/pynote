def __quickSort(alist, l, r):

    #当数列的大小比较小的时候，数列近乎有序的概率较大
    # if (r - l <= 15):
    #     insertionSortHelp(alist, l, r)
    #     return

    if l >= r:
    return
    p = partition(alist, l, r)
    # p = partitionQS(alist, l, r)

    __quickSort(alist, l, p-1)
    __quickSort(alist, p+1, r)

# 在alist[l...r]中寻找j,使得alist[l...j] <= alist[l], alist[j+1...r] >alist[l]
def partition(alist, l, r):
    pos = randint(l, r)
    alist[pos], alist[l] = alist[l], alist[pos]
    v = alist[l]
    # v = alist[l]
    j = l
    i = l + 1
    while i <= r:
    if alist[i] <= v:
      alist[j+1],alist[i] = alist[i],alist[j+1]
      j += 1
    i += 1
    alist[l], alist[j] = alist[j], alist[l]
    return j