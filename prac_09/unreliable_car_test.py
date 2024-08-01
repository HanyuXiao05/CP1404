from prac_09.unreliable_car import UnreliableCar

good_car = UnreliableCar("Good", 100, 90)
bad_car = UnreliableCar("Bad", 100, 9)

for i in range(1, 10):
    print(f"Drive {i}km:")
    print(f"{good_car.name} drove {good_car.drive(i)}km")
    print(f"{bad_car.name} drove {bad_car.drive(i)}km")

print(good_car)
print(bad_car)
