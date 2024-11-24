import math

radius = float(input("Радіус кола:"))

area = round(math.pi * radius ** 2, 14)
circumference = round(2 * math.pi * radius, 14)

print(f"площа круга: {area}")
print(f"довжина кола: {circumference}")
