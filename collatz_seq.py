import sys
from collatz import collatz

def main():
  print("Let's explore the Collatz Sequence. Enter a number that is any integer to begin the sequence.")
  n = input()
  print("Collatz Sequence starting at", n)
  try:
    number = int(n)   # n is a string so it must be converted to a integer
  except ValueError:
    print("You did not enter an integer.")
    sys.exit()

  while True:
    if number:
      print(number)
      if number == 1:
        break
    number = collatz(number)

if __name__ == '__main__':
  main()
