
def convert_seconds(seconds):
    days = seconds // 86400  
    seconds %= 86400         

    hours = seconds // 3600  
    seconds %= 3600          

    minutes = seconds // 60  
    seconds %= 60            

    return f"{days} day(s), {hours} hour(s), {minutes} minute(s), {seconds} second(s)."

inputs = [6785, 456789, 86401]


for sec in inputs:
    print(convert_seconds(sec))
