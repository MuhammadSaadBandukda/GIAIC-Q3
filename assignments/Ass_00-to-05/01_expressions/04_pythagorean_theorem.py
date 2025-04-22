import math

def find_hypotenuse(side1,side2):
  hypotenuse:float = math.sqrt(math.pow(side1,2) + math.pow(side1,2))
  return hypotenuse

def main():
  AB :float = float(input("Enter the length of a side triangle: "))
  AC :float = float(input("Enter the length of another side triangle: "))
  BC :float = round(find_hypotenuse(AB,AC),2)
  print(f"{BC} is th hypotenuse of your triangle")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

