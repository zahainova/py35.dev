def roll(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]

result1 = roll([1, 2, 3, 4, 5], 2)
print(result1) 

result2 = roll([1, 2, 3, 4, 5], -2)
print(result2) 