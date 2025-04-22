C = 299792458

def find_energy(mass):
  e = mass * (C**2)
  return e



def main():
  mass:float = float(input("Enter kilos of mass: "))
  print("e = m * C^2")
  print(f"m = {mass}")
  print(f"C = {C}")
  print(f"{find_energy(mass)} + joules of energy")



# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()