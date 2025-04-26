def main():
    for i in range(-10,0):
        print(-i,end="  ")
    print("Liftoff!",end="  ")
    print()

    for i in range(1,11).__reversed__():
        print(i,end="  ")
    print("Liftoff!",end="  ")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()