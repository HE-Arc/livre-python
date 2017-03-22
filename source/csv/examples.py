"""Exemple."""

# func:import

import csv

# endfunc:import


# func:read

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

# endfunc:read


# func:readcol

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row[2])

# endfunc:readcol


# func:write

with open('write.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["abc", "def", "ghi"])
    writer.writerow(["123", "456", "789"])

# endfunc:write


# func:readdialect

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')

# endfunc:readdialect

# func:readdialectclass


class MyDialect(csv.Dialect):
    """Redéfini les attributs de la classe Dialect."""

    delimiter = ";"
    quotechar = '"'
    escapechar = None
    doublequote = None
    lineterminator = "\r\n"
    quoting = csv.QUOTE_NONE
    skipinitialspace = False


with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, MyDialect())

# endfunc:readdialectclass
