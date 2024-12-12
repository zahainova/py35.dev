with open("sales.txt", "r") as file:
    lines = file.readlines()

for index, line in enumerate(lines, start=1):
    if "laptop" in line:
       print(f"Line {index}: {line.strip()}")

         