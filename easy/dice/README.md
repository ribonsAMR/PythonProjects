# Dice rolling
## References:
- `Random` module:	https://docs.python.org/3/library/random.html
- `Random.choice`:	https://docs.python.org/3/library/random.html#random.choice
- `str.lower()`: 		https://docs.python.org/3.6/library/stdtypes.html#str.lower

## How to use:
`python3 dice.py`

You will be asked for an input to stop or continue rolling: `"Roll? [y]/n: "`, and the default choice is **yes**.

## The Design:

### Entery point:
Line 14:
```
while True:
		user_input = input("Roll? [y]/n: ")
```
