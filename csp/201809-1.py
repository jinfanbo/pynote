n = int(input())
price = list(map(int, input().split()))
new_price = []
len_price = len(price)
new_price.append((price[0] + price[1]) // 2)
for i in range(1, len_price-1):
    new_price.append((price[i-1] + price[i] + price[i+1]) // 3)
new_price.append((price[-1] + price[-2]) // 2)
for i in new_price:
    print(i, end=' ')
