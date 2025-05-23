class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        f = (c * 9/5) + 32
        return f

print(f" Converted Temp is {TemperatureConverter.celsius_to_fahrenheit(32)}")