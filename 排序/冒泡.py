def bubble(alist):
    a = len(alist)
    for i in range(a-1, 0, -1):
        exchange = False
        for j in range(0, i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                exchange = True
        if not exchange:
            break
    return alist

if __name__ == '__main__':
    a = [1,2,4,5,23,4,5,7,76,4]
    print(bubble(a))