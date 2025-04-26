AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: " + AFFIRMATION)

    user_response = input()  # Get user's input
    while user_response != AFFIRMATION:  
        print("That was not the affirmation.")

        print("Please type the following affirmation: " + AFFIRMATION)
        user_response = input()

    print("That's right! :)")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()