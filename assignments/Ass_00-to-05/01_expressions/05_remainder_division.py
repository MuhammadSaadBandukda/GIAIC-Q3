def main():
  num1:int = int(input("Please enter an integer to be divided: "))
  num2:int = int(input("Please enter an integer to divide by: "))
  quotient :int = num1//num2
  remainder:int = num1%num2
  print(f"The result of this division is {quotient} with a remainder of {remainder}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()