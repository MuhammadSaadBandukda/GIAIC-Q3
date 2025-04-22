def main():
  adjective = input("Please type an adjective and press enter: ")
  noun = input("Please type an noun and press enter: ")
  verb = input("Please type an verb and press enter: ")
  SENTENCE_START = f"Code in Place is fun. I learned to program and used Python to make my {adjective} {noun} {verb}!"
  print(SENTENCE_START)
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()