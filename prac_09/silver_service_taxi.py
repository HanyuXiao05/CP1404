from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A Silver Service Taxi object"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """construct a SilverServiceTaxi object with name ,fuel and fanciness"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """return a string representation of a SilverServiceTaxi"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get the current fare."""
        return self.flagfall + super().get_fare()