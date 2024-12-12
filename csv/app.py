#

import csv

data = [
 [1,2,3],

]

with open('test.csv', newline='') as f:
 writer = csv.writer(f)
 writer.writerows(data)
 print(row)


with open('data1.csv', newline='w') as f:
 writer = csv.writer(f)
 writer.writerows(data)
