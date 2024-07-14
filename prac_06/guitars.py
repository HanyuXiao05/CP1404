from prac_06.guitar import Guitar

VINTAGE_STRING = '(vintage)'

guitars = []

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print('My guitars!')
name = input('Name: ')
while name != '':
    year = input('Year: ')
    cost = input('Cost: $')
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)
    print(new_guitar)
    name = input('Name: ')

print('These are my guitars:')
max_guitar_name_length = max([len(i.name) for i in guitars])
max_guitar_cost_length = max([len(f'{i.cost:,.2f}') for i in guitars])
for i, guitar in enumerate(guitars, 1):
    vintage_string = VINTAGE_STRING if guitar.is_vintage() else ''
    print(f"Guitar {i}: {guitar.name:>{max_guitar_name_length}} ({guitar.year}), worth $ {guitar.cost:>{max_guitar_cost_length},.2f} {vintage_string}")
