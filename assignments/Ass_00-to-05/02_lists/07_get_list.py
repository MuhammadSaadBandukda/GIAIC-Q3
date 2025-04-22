def main():
    items = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        items.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    print(items)

if __name__ == '__main__':
    main()