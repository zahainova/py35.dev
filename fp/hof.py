
nums = [-2, -1, 0, 1, 2]
p_num = filter(lambda n:n>0, nums)

print(p_num)

print(list(p_num))

numbers = [1, 3, 10, 45, 6, 50]

def even(n):
    e_n = []
    for i in n:
        if i %2 ==0:
           e_n.append(i)
    return e_n

print (even(numbers)) 

def is_even(n):
    return n%2 == 0

print(list(filter(is_even, numbers)))

print(list(filter(is_even, range(100))))

print(list(filter(lambda x: x% 2 == 0, range(100))))

print(list(filter(lambda x: x > 50, range(100))))

import math 

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print(list(filter(is_prime, range(1, 51))))

import statistics as st

sample = [10, 8, 10, 8, 2, 7, 9, 3, 44, 9, 8, 10, 5, 76]

mean = st.mean(sample)
print(mean)

