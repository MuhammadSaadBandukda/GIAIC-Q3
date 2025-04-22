def fahrenheit_to_celcius(degrees_fahrenheit:float):
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
    return degrees_celsius



def main():
    temperature:float = float(input("Enter temperature in Fahrenheit: "))
    fahrenheit_tempertaure:float = fahrenheit_to_celcius(temperature)
    print(f"Temperature: {temperature} = {fahrenheit_tempertaure}C")     

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

 