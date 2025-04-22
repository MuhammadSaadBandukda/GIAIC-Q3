def main():
    numbers = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        numbers.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")

    get_first_element(numbers)
    numbers = []
    get_first_element(numbers)


def get_first_element(lst:list):
    if(lst.__len__() == 0):
        print("list is empty kindly provide an unempty list" )
    else:
        for i in range(lst.__len__()):
            if(i==lst.__len__()-1):
                print("the last element of list is ", lst[lst.__len__()-1])

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()