import random

global count, word, mask, success

wordlist = "hangman ronaldo messi salah".split()

# wordlist = open('filename.txt').read()


def findall(word: str, char: str) -> list or bool:
  if char in word:
    """
        Next line explained:
        result = list()
        for i in enumerate(word): # enumerate returns tuple of index and value
                result.append(i)

        result = filter(lambda i: i[1] == char, result) # filter only the
        matched characters
    """
    result = filter(lambda i: i[1] == char, [i for i in enumerate(word)])
    return list(result)
  else:
    return False


def edit_mask(word: str, char: str):
  global mask, success
  for i in findall(word, char):
    mask[i[0]] = i[1]
    success += 1


def cleanup():
  global count, word, mask, success
  success = 0
  word = random.choice(wordlist)
  mask = mask = list("_" * len(word))
  count = int(len(word) * 1.5)


def printable_mask():
  return ' '.join(mask)


cleanup()


def main():
  global count

  try:
    while True:
      if '_' not in mask:
        print("\nYou won!")
        print("The word was: %s\n" % word)
        cleanup()
        continue

      if count == 0 or count < len(word) - success:
        print("\nYou lost, try again.")
        print("The word was: %s\n" % word)
        cleanup()
        continue

      print(printable_mask(),
            "[Tries left: %d]" % (count - (len(word) - success)))

      char = input("Your guess: ")
      char = char[0] if len(char) > 0 else None

      if not char:
        continue

      if char not in mask:
        if char in word:
          edit_mask(word, char)
      else:
        print("Guessed before.")
        continue

      count -= 1

  except KeyboardInterrupt:
    print("\nGoodbye! 👋")
    exit(0)


if __name__ == '__main__':
  main()
