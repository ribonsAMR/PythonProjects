# Dice rolling

## References:

- `random` module:	https://docs.python.org/3/library/random.html
- `random.choice`:	https://docs.python.org/3/library/random.html#random.choice

## How to use:

`python3.6 dice.py`, Change it to your Python version. Latest version is recommended.

You will be asked for an input to stop or continue rolling: `"Roll? [y]/n: "`, and the default choice is **yes**.

<hr>

# The Design:
### Entry point - `main()` function:
1. The program loops till the user enters **"n"** to stop it.

  ```python
  while True:
    user_input = input("Roll? [y]/n: ")
  ```

2. Here the program checks if the user wants to stop it, by raising the `KeyboardInterrupt` exception, It will exit properly instead of duplicating the exit code twice.

  ```python
  if user_input.lower() == "n":
    raise KeyboardInterrupt # execute the exception and quit properly.
  ```
3. **The KeyboardInterrupt Exception Handler:**

  ```python
  except KeyboardInterrupt:
    print("\nGoodbye! 👋")
    exit(0)
  ```

### Random choice:
1. We import the `random` in the beginning.

2. Initialize a variable called faces with numbers from `1 to 6` in
  ```python
  faces = [1, 2, 3, 4, 5, 6]
  # alternative: faces = list(range(1, 7))
  ```

3. We randomly generate an item from `face` variable `random.choice(faces)` (Please check `random.choice()` reference above)
