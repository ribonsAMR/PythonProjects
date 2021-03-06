import random


def guess(start=1, limit=10):
  return random.randint(start, limit)


def safely_strint(_str):
  try:
    return int(_str)
  except:
    print("Invalid input")
    return False


print("Enter quit to stop the program")


def main():
  try:
    while True:
      start, end = 0, 20
      number = guess(start, end)

      """
            String formating, please check this link: https://pyformat.info
            Alternative: input("I guessed a number from {} to {}, what is it? : ".format(start, end))
            """  # NOQA

      user_answer = input("I guessed a number from %d to %d, what is it? : " %
                          (start, end))  # NOQA

      if not user_answer:
        continue

      if user_answer.lower() == "quit":
        # execute the exception and quit properly.
        raise KeyboardInterrupt

      # convert the input to int type.
      user_answer = safely_strint(user_answer)

      if not start <= user_answer <= end:
        print("Your guess is off the limits.")
        continue

      if user_answer == number:
        print("Correct! %d" % number)
      else:
        print("Wrong, it was %d, try again." % number)
  except KeyboardInterrupt:  # CTRL+C
    print("\nGoodbye! 👋")
    exit(0)


if __name__ == '__main__':
  main()
