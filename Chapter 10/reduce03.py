from functools import reduce

result = reduce((lambda x, y: x * y), [1, 2, 3, 4], 3)

print(result)  # 72
