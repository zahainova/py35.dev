days = int(input("Days:"))
hours = int(input("Hours:"))
minutes = int(input("Minutes:"))
seconds = int(input("Seconds:"))

total_seconds = (days * 24 * 60 *60) + (hours * 60 * 60) + (minutes * 60) + seconds


print(f"The amounts of seconds: {total_seconds}")