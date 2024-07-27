import csv
from prac_07.guitar import Guitar

FILENAME = 'guitars.csv'
guitars = []


def main():
    """A program to display guitars and ask user for adding a new one"""
    read_csv_file()
    display_guitar()
    guitars.sort()
    display_guitar()
    add_new_guitar()
    display_guitar()
    save_csv_file()


def read_csv_file():
    """read csv file and store the data"""
    with open(FILENAME, 'r') as in_file:
        reader = csv.reader(in_file)
        for i in reader:
            guitars.append(Guitar(i[0], int(i[1]), float(i[2])))


def display_guitar():
    """use a for loop to display guitars"""
    for guitar in guitars:
        print(f'{guitar.name} ({guitar.year}) : ${guitar.cost:.2f})')


def add_new_guitar():
    """use a while loop to ask user for adding a new guitar until input nothing"""
    name = input("Name: ")
    while name != '':
        year = input('Year: ')
        cost = input('Cost: $')
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        name = input('Name: ')


def save_csv_file():
    """save the data to csv file"""
    with open(FILENAME, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            print(f"{guitar.name}, {guitar.year}, {guitar.cost}", file=out_file)


main()
