def main():
    empty_list = []
    print("List before",empty_list)
    add_three_copies(empty_list)
    print("List after",empty_list)

def add_three_copies(data:list):
    user_input = input("Enter a message to copy:")
    for i in range(3):
        data.append(user_input)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()