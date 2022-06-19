import csv
import numbers
from tokenize import Number

dict_from_csv = {}

""" with open('003_muska_imena.csv', mode='r') as inp: """
""" with open('003_zenska_imena.csv', mode='r') as inp: """
with open('003_prezimena.csv', mode='r') as inp:
    reader = csv.reader(inp)
    dict_from_csv = {rows[0]: int(rows[1]) for rows in reader}

print(dict_from_csv)
