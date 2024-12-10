def is_symmetrical(string):
    if len(string) % 2 != 0:
        return "The entered string is not symmetrical"
    

    mid = len(string) // 2
    first_half = string[:mid]
    second_half = string[mid:]
    

    if first_half == second_half:
        return "The entered string is symmetrical"
    else:
        return "The entered string is not symmetrical"

input_string = "khokho"
result = is_symmetrical(input_string)
print(result)