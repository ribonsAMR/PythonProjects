# Hangman
## References:
- `Random` module:			https://docs.python.org/3/library/random.html
- `Random.choice`:			https://docs.python.org/3/library/random.html#random.choice
- `str.split()` method:		https://docs.python.org/3/library/stdtypes.html?#str.split
- `str.join()` method:		https://docs.python.org/3.6/library/stdtypes.html#str.join
- Functions annotations:	https://www.python.org/dev/peps/pep-3107/
- Variable annotations:		https://www.python.org/dev/peps/pep-0526/
- `filter` function:			https://docs.python.org/3/library/functions.html#filter
- `lambda` expression:		https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
  `lambda` simple tutorial:	https://www.programiz.com/python-programming/anonymous-function
- `Global` statment:			https://docs.python.org/3.6/reference/simple_stmts.html#the-global-statement
- String formating:			https://pyformat.info
- `KeyboardInterrupt`:		https://docs.python.org/3.6/library/exceptions.html#KeyboardInterrupt

## How to use:
`python3.6 hangman.py`, Change it to your Python version. Latest version is recommended.

You will be presented with a mask of the word, and the tries left before losing.<br>
The tries are dynamically changing according to the left tries and the unknown characters.

You can use text files for the `wordlist` variable in this line: `wordlist = "hangman ronaldo messi salah".split()`, replace it with the file content code: `open("filename").read()`

And adjust how the words are extracted from the file to create a list of separate words.

To stop the game, press CTRL+C.

<hr>

# The Design:
- ### Entry point:
	1. The program loops till the user stops it using CTRL+C.

	2. The game starts with calling `cleanup()` function, which is used in other parts too.

	#### `Cleanup()` function:
	1. Initialize global variables `count, word, mask, success`

	2. `success` counts the correctly guessed characters.

	3. mask is the hidden word form: `-----`.

	4. count is number of tries and it dynamically changes for every word by multiplying the words length by 1.5.

	5. `word = random.choice(wordlist)`, Randomly choose a word from the `wordlist` variable above.

	6. `mask = list("-" * len(word))`, create a list of dashes according to the word's characters.

	```
	def cleanup():
		global count, word, mask, success
		success = 0
		word = random.choice(wordlist)
		mask = list("_" * len(word))
		count = int(len(word) * 1.5)

	cleanup()
	try:
		while True"
	```

- ### Win and lose cases:
	1. `if not '_' in mask:`, when there's no any dashes left in the mask, then the user won the game.

	2. `if count == 0 or count < len(word) - success:`, whether the original tries number equals zero, or the it's less the left unknown characters number, then, the user lost the game.

- ### Validate the input:
	1. Get only the first character from the input, If there was no input, set the `char` variable to `None`.

	2. If the `char` variable is `None` or `False`, continue the loop, because the input was empty.

	```
	char = input("Your guess: ")
	char = char[0] if len(char) > 0 else None

	if not char:
		continue
	```

- ### Validate the guess:
	1. If the character entered wasn't in the `mask`, check if it's in the `word`.

	2. If it's in the `word`, then edit the `mask` to the new look.

	3. If it's in the `mask`, then tell the user that he guessed this character before, and skip the `count` decrement.

	```
	if not char in mask:
		if char in word:
			edit_mask(word, char)
	else:
		print("Guessed before.")
		continue

	count -= 1
	```
