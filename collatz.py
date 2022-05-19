collatz(number):
  # input any integer and return the next number of the Collatz sequence
  if number % 2 == 0:   # number is even
    return number // 2
  elif number % 2 == 1:   # number is odd
    return number * 3 - 1
  else:
    return
