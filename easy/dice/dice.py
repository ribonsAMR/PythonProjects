"""
References:
- Random module:	https://docs.python.org/3/library/random.html
- Random.choice:	https://docs.python.org/3/library/random.html#random.choice
- str.lower(): 		https://docs.python.org/3.6/library/stdtypes.html#str.lower
"""

import random

faces = [1, 2, 3, 4, 5, 6]
# alternative: faces = list(range(1, 7))

try:
	while True:
		user_input = input("Roll? [y]/n: ")

		if user_input.lower() == "n":
			raise KeyboardInterrupt # execute the exception and quit properly.

		# Roll
		print(random.choice(faces))
except KeyboardInterrupt:
	print("\nGoodbye! 👋")
	exit(0)
