from decimal import Decimal, getcontext

getcontext().prec = 10

def complex_interest(principal, rate, times_compounded, years):
  
    P = Decimal(principal)
    r = Decimal(rate)
    n = Decimal(times_compounded)
    t = Decimal(years)
    
    A = P * (1 + (r / n)) ** (n * t)
    
    return A

principal = 1000  
rate = 0.05       
times_compounded = 4  
years = 5         

final_amount = complex_interest(principal, rate, times_compounded, years)
print(f"The accumulated amount after {years} years is: {final_amount:.2f}")
