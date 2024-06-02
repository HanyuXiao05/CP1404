items_num = int(input('items amount: '))
total = 0

while items_num < 0:
    print('Invalid number of items!')
    items_num = int(input('items amount: '))

for i in range(items_num):
    price = float(input('Price of item: '))
    total += price

if total > 100:
    total *= 0.9

print(f"Total price for {items_num} items is ${total:.2f}")