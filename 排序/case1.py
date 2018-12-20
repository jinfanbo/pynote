a = {'d': 30, 'a': 10, 'b': 20, 'c': 0}
b = sorted(a.items(), key=lambda x: x[1])
print(b)
