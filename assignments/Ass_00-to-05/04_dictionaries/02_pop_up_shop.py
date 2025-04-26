def main():
    APPLE = 5
    DURIAN = 5
    JACKFRUIT = 5
    KIWI = 5
    RAMBUTAN = 5
    MANGO = 5

    record = {"apple":[0,APPLE],
              "durian":[0,DURIAN],
              "jackfruit":[0,JACKFRUIT],
              "kiwi":[0,KIWI],
              "rambutan":[0,RAMBUTAN],
              "mango":[0,MANGO],
              }
    add = 0
    for keys,values in record.items():
        values[0] = int(input(f"How much {keys} do you want: ")) * values[1]
        add += values[0] 
        print(f"{keys} --> {values}")
    
    
    print(f"Your total bill is ${add}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()