import csv
wimbledon_to_data = {}


def main():
    '''read the csv file and print all champions, their won times and countries'''
    read_csv()
    champions = list_champions()
    countries = list_countries()
    won_times = count_won_times(champions)
    display_champions(won_times)
    display_countries(countries)


def read_csv():
    '''read csv file and store as a dictionary'''
    filename = "wimbledon.csv"
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        for i in reader:
            wimbledon_to_data[i[0]] = i[1:]


def list_countries():
    '''return a list of all countries'''
    countries = [v[0] for k, v in wimbledon_to_data.items()]
    # set method is an ideal way to clean the repeat elements, but we need a list finally
    return list(set(countries))


def list_champions():
    '''return a list of all champions'''
    champions = [v[1] for k, v in wimbledon_to_data.items()]
    return champions


def count_won_times(champions):
    '''count won times of each champion'''
    won_times = {}
    for i in champions:
        if i not in won_times:
            won_times[i] = 1
        else:
            won_times[i] += 1
    return won_times


def display_champions(won_times):
    '''display champions and their won times'''
    print('Wimbledon Champions: ')
    for name, times in won_times.items():
        print(name, times)


def display_countries(countries):
    '''display won countries'''
    countries.sort()
    print(f'These {len(countries)} countries have won Wimbledon:')
    print(', '.join(countries))


main()