"""Exemple."""

# func:import

import csv

# endfunc:import

# func:read

with open('data.csv', 'rt') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

# endfunc:read

# func:readcol

with open('data.csv', 'rt') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row[2])

# endfunc:readcol

# func:write

with open('write.csv', 'wt') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["abc", "def", "ghi"])
    writer.writerow(["123", "456", "789"])

# endfunc:write
