# Guess The number

## References:

**General references [here](/../../#general-references-important)**

- `random` module: 	https://docs.python.org/3/library/random.html
- `random.randint`: 	https://docs.python.org/3.6/library/random.html#random.randint

## How to use:
`python3.6 guessthenumber.py`, Change it to your Python version. Latest version is recommended.

You will be asked to input your guess or **"quit"** to exit the game.
<br>The game guesses a number from 0 to 20, you can change it from this line `start, end = 0, 20`.

<hr>

# The Design:
### Entry point - `main()` function:
  1. The program loops till the user stops it.

  2. The default range of guessing is `0 to 20`, then we call the `guess` function
  passing these arguments.

  3. The `guess` function returns a random number using `randint` function from
  the `random` module (Please check the references).

  ```python
  def guess(start=1, limit=10):
    return random.randint(start, limit)

  try:
    while True:
      start, end = 0, 20
      number = guess(start, end)
  ```

### Checking the input validity:
  1. Taking the input from the user and check if it is **quit** to stop the program by raising the `KeyboardInterrupt` exception, if not, continue.

  2. Try to convert the user's input to an integer type value, using the `safely_strint` function, It returns an integer or `False`.

  ```python
  def safely_strint(_str):
    try:
    	return int(_str)
    except Exception as e:
    	print("Invalid input")
    	return False

  user_answer = input("I guessed a number from %d to %d, what is it? : " %(start, end))

  if user_answer.lower() == "quit":
    raise KeyboardInterrupt

  user_answer = safely_strint(user_answer)
  ```

### Comparing the input with the guessed number:
  1. First, we check if the input is off the limits and warn the user then cancel the current loop and continue.

  2. If not off the limits, we compare them together and tells the user if the guess was correct or not.

  ```python
  if not start <= user_answer <= end:
    print("Your guess is off the limits.")
    continue

  if user_answer == number:
    print("Correct! %d" %number)
  else:
    print("Wrong, it was %d, try again." %number)
  ```

### KeyboardInterrupt Exception Handler:
  I put the exit code inside the `KeyboardInterrupt` exception handler and raise it when the user wants to quit, with exit code 0.
  <br>

  ```python
  except KeyboardInterrupt: # CTRL+C
    print("\nGoodbye! 👋")
    exit(0)
  ```
