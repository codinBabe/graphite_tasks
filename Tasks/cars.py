class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage:,} miles"
    

if __name__ == "__main__":
    blue = Car("blue", 20_000)
    red = Car("red", 30_000)
    print(blue)
    print(red)