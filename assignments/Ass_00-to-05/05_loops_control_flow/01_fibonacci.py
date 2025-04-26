MAX_VALUE = 10000
def main():
    prev = 0
    nexxt = 1
    current = nexxt + prev
    while not current > MAX_VALUE:
        print(current,end="-->")
        current = prev + nexxt
        prev = nexxt
        nexxt = current
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()