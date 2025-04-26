MAX_VALU = 100
def main():
    input_num = int(input("Enter a number you want to double: "))
    while input_num <=100:
        prev_input = input_num
        input_num*=2
        print(f"{prev_input} doubled is {input_num}")
    print(f"We stopped at {input_num} because it is greater than 100")
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()