def convert_feet_to_inch(feet):
  inches = feet * 12
  return inches

def main():
  feet = float(input("Enter the length in feet to convert: "))
  print(f"Measurement of {feet} in inch is {convert_feet_to_inch(feet)}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()