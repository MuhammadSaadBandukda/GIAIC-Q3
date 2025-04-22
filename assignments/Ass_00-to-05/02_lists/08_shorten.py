MAX_LENGTH = 5
def main():
    lst:list=[1,3,4,9,0]
    print(shorten(lst))
    lst.append([289,2290])
    print(shorten(lst))

def shorten(lst:list):
    if(lst.__len__()<= MAX_LENGTH):
        print("No changes")
        return lst
    else:
        while (lst.__len__() > MAX_LENGTH):
            print(lst.pop(),"has popped")
        return lst
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()