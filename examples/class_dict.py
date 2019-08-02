class Edible:
    def eatme(self):
        print(f"{self.__class__} is being eaten.")

class FishAndChips(Edible):
    def add_sauce(self):
        print(f"Adding sauce to {self.__class__}")


cod_and_chips = FishAndChips()
print(dir(cod_and_chips))
print(type(FishAndChips.__dict__))