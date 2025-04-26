import random

def main():
    rand_num= random.randint(1,99)
    input_num= int(input("I am thinking of a number between 0 and 99... Enter a guess: ")) 
    while True:
        if rand_num == input_num:
            print("your are correct")
            break
        if input_num>rand_num:
            print("your number is high")
        elif input_num<rand_num:
            print("your number is low")
        input_num= int(input("Enter a new number: ")) 
        
            


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()