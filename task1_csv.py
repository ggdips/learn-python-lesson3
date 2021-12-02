#!env/bin/python3
import csv

mydict = [
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]

def main():
    mydictkeys = mydict[0].keys()
    expfile = open('export.csv', 'w', encoding='utf-8')
    dict_writer = csv.DictWriter(expfile, mydictkeys)
    dict_writer.writeheader()
    dict_writer.writerows(mydict)
    expfile.close()

if __name__ == "__main__":
    main()
