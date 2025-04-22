def main():
    numbers:list=[23,87,32]
    for i in range(0,numbers.__len__()):
        numbers[i] = numbers[i]*2
    print(numbers)
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()