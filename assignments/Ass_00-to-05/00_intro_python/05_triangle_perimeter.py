def tri_perimter(side1,side2,side3):
    perimter:float= side1+side2+side3
    return perimter




def main():
    side1:float = float(input("What is the length of side 1: "))
    side2:float = float(input("What is the length of side 2: "))
    side3:float = float(input("What is the length of side 3: "))

    perimeter:float = tri_perimter(side1,side2,side3)
    print(f"The perimeter of the triangle is {perimeter}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()