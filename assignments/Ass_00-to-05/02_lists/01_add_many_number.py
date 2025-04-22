def main():
    print(add([1,34,66]))
def add(li:list[int|float]):
    sum_of_all = 0
    for i in li:
        sum_of_all+=i 
    return sum_of_all

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()