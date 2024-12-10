def EMI(principal, annual_rate, months):
    """
        
    :param principal: Основна сума (P)
    :param annual_rate: Річна відсоткова ставка у відсотках (наприклад, 8 для 8%)
    :param months: Загальна кількість місяців (n)
    :return: EMI (float)
    """
    monthly_rate = annual_rate / (12 * 100)  # 8% => 0.006666...
    
    emi = principal * (monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    
    return emi


principal = 500000  
annual_rate = 8     
months = 24         

emi = EMI(principal, annual_rate, months)
print(f"EMI for {months} months: {emi:.12f}")

