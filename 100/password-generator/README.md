# Password Generator

## References:

**General references [here](/../../#general-references-important)**

- `secrets` module: https://docs.python.org/3/library/secrets.html#module-secrets
- `string` module: https://docs.python.org/3/library/string.html
- `argparse` module: https://docs.python.org/3/library/argparse.html
- `argparse` tutorial: https://docs.python.org/3/howto/argparse.html#id1

## How to use:
Usage: `python3.6 pwdgn.py [-h] [-i Ingredients] [-c count] length`

`python3.6 pwdgn.py 10 -i uld -c 10`, This will generate *10* passwords with length of *10*, the password will be made of *(u)*pper and *(l)*ower cases with *(d)*igits.

The available ingredients: *(u)*pper case, *(l)*ower case, *(d)*igits, *(p)*unctuations, just include the first character of each ingredient, eg. `ul` means upper and lower cases.

You can use just one ingredient. 

A reference to the `phrasegenerator()` function: https://docs.python.org/3/library/secrets.html#recipes-and-best-practices