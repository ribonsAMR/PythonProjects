import random

faces = [1, 2, 3, 4, 5, 6]
# alternative: faces = list(range(1, 7))

def main():
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

if __name__ == '__main__':
	main()
