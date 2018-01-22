# Dice rolling
## References:
- `Random` module:	https://docs.python.org/3/library/random.html
- `Random.choice`:	https://docs.python.org/3/library/random.html#random.choice
- `str.lower()`: 		https://docs.python.org/3.6/library/stdtypes.html#str.lower

## How to use:
`python3 dice.py`

You will be asked for an input to stop or continue rolling: `"Roll? [y]/n: "`, and the default choice is **yes**.

## The Design:
### Random:
1. We import the `random` in the beginning.
2. Initialize a variable called faces with numbers from `1 to 6` in ``` faces = [1, 2, 3, 4, 5, 6]
# alternative: faces = list(range(1, 7))
```
3. We randomly generate a number `random.choice(faces)` (Please check `random.choice()` reference above)

### Entry point:
- <b>Line 14:</b> The program loops till the user enters **"n"** to stop it.
  ```
  while True:
    user_input = input("Roll? [y]/n: ")
  ```

- **Line 17:** Here the program checks if the user wants to stop it, by raising the `KeyboardInterrupt` exception, It will exit properly instead of duplicating the exit code twice.
  ```
  if user_input.lower() == "n":
    raise KeyboardInterrupt # execute the exception and quit properly.
  ```
- **The KeyboardInterrupt Exception Handler:**
  ```
  except KeyboardInterrupt:
    print("\nGoodbye! 👋")
    exit(0)
  ```
