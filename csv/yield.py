def multi_yield():
    yield "This will print the first string"
    yield "This will print the second string"

multi_obj = multi_yield()

print(next(multi_obj)) 
print(next(multi_obj))

def fn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_n = sum(fn(100000000))
print(sum_of_n)

