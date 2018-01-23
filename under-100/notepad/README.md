# Simple Notepad

## References:
- `open()` function: 	https://docs.python.org/3/library/functions.html#open
- `KeyboardInterrupt`:	https://docs.python.org/3.6/library/exceptions.html#KeyboardInterrupt

## How to use:
`python3.6 notepad.py`.

You will be asked to enter the file name in the beginning, the script uses the `append` mode, and then you write the text you want.

`-w` to write the changes.<br>
`-c` to cancel the changes.

# The Design:
- ### Entry point - `main()`:
	1. We get the filename and store it in the `filename` variable, if the input was empty, raise the `KeyboardInterrupt` expection and exit the script properly.

		```python
		filename = input("filename (leave blank to exit): ")
			if not filename:
				raise KeyboardInterrupt
		```

	2. Now we open the file in append+ mode via the variable `f` (creates the file if it doesn't exists), and we declare a variable called `content_to_write` to store the user's data before saving or canceling the changes.

		```python
		with open(filename, 'a+') as f:
			content_to_write = ""
		```

	3. The user will keep entering text till he enters `-w` to stop it or `-w` to save the changes.

		```python
		while True:
			user_input = input("-> ")
		```

	4. By default, every loop, add the new input to the last ones.

		```python
		content_to_write += user_input + '\n'
		```

	5. And If the user enters `-w`, it writes the text in `content_to_write` to the file `f`, and breaks the loop to back to the main loop (filename loop).

		```python
		if user_input.lower() == "-w":
			f.write(content_to_write)
			print("Changes saved.")
			break
		```