import time

class PhoneBook():
    phone_book ={}
    def __init__(self,username):
        print(f"Hey {username}! Welcome to the phonebook service!, How may we help you?")
    
    def read_number(self):
        if self.phone_book == {}:
            print("Empty Phonebook")
        else:
            for keys,values in self.phone_book.items():
                print(f"{values} --> {keys}")
        time.sleep(1)

    def add_number(self):
        print("*********Adding Number*********")
        name = input("Enter a Name: ")
        number = input("Enter a Number: ")
        self.phone_book[number] = name
        print("******Added Successfully******")
        for keys,values in self.phone_book.items():
            print(f"{values} --> {keys}")
        time.sleep(1)
    
    def search_number(self):
        print("******Searching Number******")
        search_by:int = int(input("Search by 1.Name 2.Number (type number only): "))
        if search_by == 1:
            name = input("Enter the Name: ")
            for numbers,names in self.phone_book.items():
                if name == names:
                    print(f"{names} --> {numbers}")
            time.sleep(1)
        elif search_by == 2:
            number = input("Enter the Number: ") 
            for numbers in self.phone_book:
                if number == numbers:
                    print(f"{self.phone_book[numbers]} --> {numbers}")
            time.sleep(1)
        else:
            print("Invalid choice")

    def delete_number(self):
        print("******Deleting Number******")
        delete_by:int = int(input("Delete by 1.Name 2.Number (type number only): "))
        target = None
        if delete_by == 1:
            name = input("Enter the Name: ")
            for numbers,names in self.phone_book.items():
                if name == names:
                    target = numbers
            self.phone_book.pop(target)
            if self.phone_book == {}:
                print("Empty Phonebook")
            else:
                for keys,values in self.phone_book.items():
                    print(f"{values} --> {keys}")
            time.sleep(1)
    
        elif delete_by == 2:
            number = input("Enter the Number: ") 
            for numbers in self.phone_book:
                if number == numbers:
                    target = numbers
            self.phone_book.pop(target)
            time.sleep(1)
        else:
            print("Invalid choice")

def main():
    name = input("Enter your name: ")
    while True:
        a = PhoneBook(name) 
        time.sleep(1)
        print("There are 4 options:")
        print("a) Read your Phone Book")
        print("b) Add any number in your PhoneBook")
        print("c) Search from Phone Book")
        print("d) Delete a number from Phone Book")
        opt = input("Enter your choice: ")
        match(opt):
            case 'a':
                a.read_number()
            case 'b':
                a.add_number()
            case 'c':
                a.search_number()
            case 'd':
                a.delete_number()
            case _:
                print("Good bye")
                break

    

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()