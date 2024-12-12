def includes_any(lst, values):
    return bool(set(lst) & set(values))

result1 = includes_any([1, 2, 3, 4], [2, 9])
print(result1)

result2 = includes_any([1, 2, 3, 4], [8, 9])
print(result2)

