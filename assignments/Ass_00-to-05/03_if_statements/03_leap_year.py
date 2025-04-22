def main():
    year:int = int(input("Enter the year to check for a leap year: "))
    if type(year) == int:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 ==  0:
                    print("it's a leap year")
                else:
                    print("it's not a leap year")
            else:
                print("it's a leap year")
        else:
            print("it's not a leap year")




# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()