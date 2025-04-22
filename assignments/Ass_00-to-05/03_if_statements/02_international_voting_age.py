def main():
    age = int(input("How old are you?"))
    Peturksbouipo = 16
    Stanlau = 25
    Mayengua = 48
    if age < Peturksbouipo:
        print("You cannot vote in anywhere")
    elif age < Stanlau:
        print(f"You can vote in Peturksbouipo where the age is {Peturksbouipo} .You can not vote in Stanlau where the age is {Stanlau}.You can not vote in Mayengua where the age is {Mayengua}")
    elif age < Mayengua:
        print(f"You can vote in Peturksbouipo where the age is {Peturksbouipo} .You can vote in Stanlau where the age is {Stanlau}.You can not vote in Mayengua where the age is {Mayengua}")
    else:
        print(f"You can vote in Peturksbouipo where the age is {Peturksbouipo} .You can vote in Stanlau where the age is {Stanlau}.You can vote in Mayengua where the age is {Mayengua}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()