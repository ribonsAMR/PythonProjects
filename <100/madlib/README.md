# Mad Lib Game

## References:
**General references [here](/../../#general-references-important)**

- [colorama](https://pypi.python.org/pypi/colorama) library, cross-platform colored terminal text.
- `re.findall()` Method: https://docs.python.org/3/library/re.html#re.findall

## How to use:
`python3.6 madlib.py`

## The Design:

1. Importing the regex library, importing `init` function and `Fore` class from `colorama`.

	```python
	import re
	from colorama import init, Fore
	init(autoreset=True)
	```

2. Decalring a variable called `general_pattern` with the pattern to find the variables inside the text, like `<noun>`, `<verb>`, and variables starts with the hashtag `<#noun>` to follow the variable before it.

	If you have variables in order: `<noun> <#noun> <noun>`, the second variable's value will be the same as the first one's.

	```python
	general_pattern = "<#?\w+>"
	```

3. Removing <, >, and # from the variable's name, using `lambda` function. We can use the normal function too as I commented in the script.

	```python
	cleanup = lambda x: x.replace('<', '').replace('>', '').replace('#', '')
	```

4. Get all the variables inside the text inside a variable called `replace_list`

	```python
	replace_list = re.findall(general_pattern, text)
	```

5. Using the `enumerate` function to loop through the list with the knowledge of index and value at the same time, and to modify the list while looping.

	```python
	enumerate(replace_list)
	```