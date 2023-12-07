data = [x for x in range(10)]

res = (filter(lambda x: x%2 == 0, data))

print(tuple(res))