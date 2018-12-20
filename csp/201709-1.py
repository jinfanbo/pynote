n = int(input())
if n < 30:
    print(n // 10)
elif n < 50:
    print(4 + (n - 30) // 10)
else:
    a = n // 50
    b = (n-50*a) // 30
    c = (n-50*a-30*b) // 10
    print(a*(5+2) + b*(3+1) + c)
