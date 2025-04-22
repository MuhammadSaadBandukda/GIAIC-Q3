def add(num_1,num_2):
    if(type(num_1) is (int or float)) and (type(num_2) is (int or float)):
        sum = num_1 + num_2
        return sum
    else:
        print("your input should be numerical")

def main():
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    # number1 = int(number1)
    # number2 = int(number2)
    # print("type of num1 is ", type(number1 ) )
    # print("type of num2 is ", type(number2 ) )
    print("The sum of numbers is " ,add(number1,number2))


if __name__ == '__main__':
    main()