def main():
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    get_first_element(lst)
    lst = []
    get_first_element(lst)




    return lst


def get_first_element(lst:list):
    if(lst.__len__() == 0):
        print("list is empty kindly provide an unempty list" )
    else:
        print("the first element of list is ", lst[0])

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()