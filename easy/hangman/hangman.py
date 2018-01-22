"""
References:
- Random module:			https://docs.python.org/3/library/random.html
- Random.choice:			https://docs.python.org/3/library/random.html#random.choice
- str.split() method:		https://docs.python.org/3/library/stdtypes.html?#str.split
- str.join() method:		https://docs.python.org/3.6/library/stdtypes.html#str.join
- Functions annotations:	https://www.python.org/dev/peps/pep-3107/
								They are just for explaining the code,
								removing them won't affect the script.
- Variable annotations:		https://www.python.org/dev/peps/pep-0526/
								As functions annotations, not necessary too
								and can be removed.
- filter function:			https://docs.python.org/3/library/functions.html#filter
- lambda expression:		https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
  lambda simple tutorial:	https://www.programiz.com/python-programming/anonymous-function
- Global statment:			https://docs.python.org/3.6/reference/simple_stmts.html#the-global-statement
- String formating:			https://pyformat.info
- KeyboardInterrupt:		https://docs.python.org/3.6/library/exceptions.html#KeyboardInterrupt
"""

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

		result = filter(lambda i: i[1] == char, result) # filter only the matched characters
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

try:
	while True:
		if not '_' in mask:
			print("\nYou won!")
			print("The word was: %s\n" %word)
			cleanup()
			continue
			
		if count == 0 or count < len(word) - success:
			print("\nYou lost, try again.")
			print("The word was: %s\n" %word)
			cleanup()
			continue

		print(printable_mask(), "[Tries left: %d]" %(count - (len(word) - success)))

		char = input("Your guess: ")
		char = char[0] if len(char) > 0 else None

		if not char:
			continue

		if not char in mask:
			if char in word:
				edit_mask(word, char)
		else:
			print("Guessed before.")
			continue

		count -= 1

except KeyboardInterrupt:
	print("\nGoodbye! 👋")
	exit(0)
