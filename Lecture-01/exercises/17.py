
s = float(input("нарахована платня (грн): "))  
p = float(input("податок (%): ")) 

net_salary = s * (1 - p / 100)

print(net_salary)
