import secrets
import string
import argparse


def phrasegenerator(file, length=4):
  with open(file, 'r') as f:
    words = [word.strip() for word in f.readlines()]
    return ''.join(secrets.choice(words) for i in range(4))


def generator(length=8, ingre="uld"):
  ingredients = ""
  ingredients += string.ascii_uppercase if 'u' in ingre else ""
  ingredients += string.ascii_lowercase if 'l' in ingre else ""
  ingredients += string.digits if 'd' in ingre else ""
  ingredients += string.punctuation if 'p' in ingre else ""
  ingredients = ingredients or ingre
  return ''.join(secrets.choice(ingredients) for _ in range(length))


def main():
  # print(generator())
  # print(phrasegenerator("wordlist.txt"))

  parser = argparse.ArgumentParser()
  parser.add_argument(
      "-i",
      metavar="Ingredients",
      help="Ingredients [u, l, d, p]: Upper, lower, digits and punctuations."
  )  # NOQA
  parser.add_argument("-c", default=1, type=int, metavar="count")
  parser.add_argument(
      "length",
      default=8,
      type=int,
      help="Length of the password, the default is 8.")

  args = parser.parse_args()

  for _ in range(args.c):
    print(generator(args.length, args.i or "uld"))


if __name__ == '__main__':
  main()
