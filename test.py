# set_a: set[int] = {1, 2, 3, 4, 5}
# set_b: set[int] = {4, 5, 6, 7, 8}

# print("Set union", set_a | set_b)
# print("Set difference", set_a - set_b)
# print("Set intersection", set_a & set_b)
# print("Unique elements or Symmetric difference or A⋃B - A⋂B", set_a ^ set_b)

class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False
    
    def turn_on(self) -> None:
        if self.turned_on:
            print(f'Microwave ({self.brand}) is already turned on.')
        else:
            self.turned_on = True
            print(f'Mircrove ({self.brand}) is now turned on.')

    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False
            print(f'Microwave ({self.brand}) is now turned off.')
        else:
            print(f'Mircrove ({self.brand}) is already off.')

smeg: Microwave = Microwave('Smeg', 'B')

smeg.turn_on()
smeg.turn_on()

smeg.turn_off()
smeg.turn_off()