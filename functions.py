def add(*args):
    return sum(args)

print(add(1, 2))
print(add(5, 10, 15))
print(add(100))
# Part 2 — lambda
numbers = [3, 1, 4, 1, 5, 9]
sorted_nums = sorted(numbers, key=lambda x: x)
print(sorted_nums)