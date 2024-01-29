numbers = [1, 2, 3, 4, 5]

squared_nums = list(map(lambda x: x**2, numbers))
print(squared_nums)

nums = [1, 2, 3, 4, 5]
squared_nums = [x * x for x in nums]
print(squared_nums)
