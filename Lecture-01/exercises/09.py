def calculate_deposit(future_value, annual_rate, years):
    """
    Розраховує поточну суму, яку потрібно внести на депозит.
    
    :param future_value: f
    :param annual_rate: r
    :param years: n
    :return: p 
    """
    
    present_value = future_value / ((1 + annual_rate) ** years)
    return present_value


future_value = float(input("Enter the desired future value: "))
annual_rate = float(input("Enter the annual interest rate (as a decimal): "))
years = int(input("Enter the number of years the money will grow: "))


present_value = calculate_deposit(future_value, annual_rate, years)


print(f"You will need to deposit this amount: {present_value:.2f}")
