#!/bin/python3

class Coffee:
    def __init__(self, vol, cost):
        self._volume = vol
        self._price = cost
    
    def __repr__(self):
        return f"Coffee({self._volume}, {self._price})"
    
    def __str__(self):
        return f"This coffee costs ${self._price} and is {self._volume}ml"
    
    def __add__(self, other):
        if isinstance(other, Coffee):
            new_coffee = Coffee(self._volume + other._volume,
                                self._price + other._price)
            return new_coffee
        else:
            raise TypeError("Unsupported operand type(s) for +")

    def __eq__(self, other):
        return self._volume == other._volume and self._price == other._price

    def __le__(self, other):
        return self._volume <= other._price

    def __lt__(self, other):
        return self._volume < other._price

    def __ge__(self, other):
        return self._volume >= other._volume

    def __gt__(self, other):
        return self._volume > other._volume

small_coffee = Coffee(120, 1.50)
large_coffee = Coffee(360, 2.25)
same_coffee = Coffee(120, 1.00)

print("Small coffee: 120 mL, $1.50")
print("Large coffee: 360 mL, $2.25")
print("Same coffee: 120 mL, $1.00")

print(small_coffee + large_coffee)

print("Testing small_coffee == large_coffee:", small_coffee == large_coffee)
print("Testing same_coffee == small_coffee:", same_coffee == small_coffee)
print("Testing same_coffee >=, >, <=, and < small_coffee:", same_coffee >= small_coffee, same_coffee > small_coffee, small_coffee <= same_coffee, small_coffee < same_coffee)
