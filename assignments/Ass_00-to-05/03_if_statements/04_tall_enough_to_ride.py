import time

def main():
    def tall_enough_extension():
        while True:
            height:int= input("Enter Your height: ")
            if not height == "":
                height = int(height)
                if height >=50:
                    print("You're tall enough to ride!")
                else:
                    print("You're not tall enough to ride, but maybe next year!")
            else:
                print("program is terminating due to invald input..." ,end="")
                time.sleep(1)
                return
    tall_enough_extension()


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()