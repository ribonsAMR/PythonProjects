# Hangman
## References:
- `Random` module:			https://docs.python.org/3/library/random.html
- `Random.choice`:			https://docs.python.org/3/library/random.html#random.choice
- `str.split()` method:		https://docs.python.org/3/library/stdtypes.html?#str.split
- `str.join()` method:		https://docs.python.org/3.6/library/stdtypes.html#str.join
- Functions annotations:	https://www.python.org/dev/peps/pep-3107/
								They are just for explaining the code,
								removing them won't affect the script.
- Variable annotations:		https://www.python.org/dev/peps/pep-0526/
								As functions annotations, not necessary too
								and can be removed.
- `filter` function:			https://docs.python.org/3/library/functions.html#filter
- `lambda` expression:		https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
  `lambda` simple tutorial:	https://www.programiz.com/python-programming/anonymous-function
- `Global` statment:			https://docs.python.org/3.6/reference/simple_stmts.html#the-global-statement
- String formating:			https://pyformat.info
- `KeyboardInterrupt`:		https://docs.python.org/3.6/library/exceptions.html#KeyboardInterrupt

## How to use:
`python3 hangman.py`

You will be presented with a mask of the word, and the tries left before losing.<br>
The tries are dynamically changing according to the left tries and the unknown characters.

You can use text files for the `wordlist` variable in this line: `wordlist = "hangman ronaldo messi salah".split()`, replace it with the file content code: `open("filename").read()`<br>and adjust how the words are extracted from the file.

To stop the game, press CTRL+C.