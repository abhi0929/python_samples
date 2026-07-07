class Temperature:

    def __init__(self, celsius):
        self.celsius = celsius

    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    def show_conversion(self):
        print("Celsius:", self.celsius)
        print("Fahrenheit:", Temperature.to_fahrenheit(self.celsius))


t = Temperature(30)
t.show_conversion()