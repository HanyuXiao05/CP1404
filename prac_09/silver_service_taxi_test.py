from prac_09.silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi('Test', 100, 2)
my_taxi.drive(18)
assert my_taxi.get_fare() == 48.78
