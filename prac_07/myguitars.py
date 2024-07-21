import csv
from prac_07.guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    guitars = read_csv_file()
    guitars.sort()
    for guitar in guitars:
        print(guitar.name)


def read_csv_file():
    """read csv file and store the data"""
    guitars = []
    with open(FILENAME, 'r') as in_file:
        reader = csv.reader(in_file)
        for i in reader:
            guitars.append(Guitar(i[0], int(i[1]), float(i[2])))
    return guitars


main()
