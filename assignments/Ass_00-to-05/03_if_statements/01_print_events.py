def main():
    # first very fast approach 
    for i in range(20):
        print(i*2)
    # second
    for i in range(40):
        if i%2 == 0:
            print(i)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()