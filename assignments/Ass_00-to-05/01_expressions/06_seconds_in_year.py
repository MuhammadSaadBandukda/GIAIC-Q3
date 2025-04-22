def main():
  DAY = 365
  HOUR = 24
  MINUTE = 60
  SECOND = 60

  year = float(input("Enter the year to convert in second:"))
  days = year * DAY
  hours = year * DAY * HOUR
  minutes = year * DAY * MINUTE
  seconds = year * DAY * MINUTE * SECOND

  print(f"{year} year(s) have:")
  print(f"{days} days")
  print(f"{hours} hours")
  print(f"{minutes} minutes")
  print(f"{seconds} seconds")
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()