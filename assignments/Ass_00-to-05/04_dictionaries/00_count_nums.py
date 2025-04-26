import time
def main():
    record = {}
    while True:
        num:str = input("Enter a numer: ")
        if num.isnumeric():
            num = int(num)
            if num in record:
                record[num]+=1
            else:
                record.update({num:1})
        elif num == '':
            for key,value in record.items():
                print(f"{key} appears {value} times")
            print("program is terminating...")
            time.sleep(1)
            break
        else:
            print("Invaid output")
    
    

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()