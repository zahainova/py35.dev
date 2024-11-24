n = int(input("Введіть число хвилин:"))

minutes_in_day = 1440

minutes_passed_today = n % minutes_in_day

hours = minutes_passed_today // 60
minutes = minutes_passed_today % 60

print(f"{hours} {minutes}")