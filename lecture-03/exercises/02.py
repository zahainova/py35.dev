def min_n(lst, n):
    if n >= len(lst):
        return sorted(lst)
    return sorted(lst)[:n]

result1 = min_n([1, 2, 3], 1)
print(result1)

result2 = min_n([1, 2, 3], 2)
print(result2) 