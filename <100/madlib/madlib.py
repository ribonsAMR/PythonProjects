import re
from colorama import init, Fore
init(autoreset=True)

# This pattern finds <noun> and <#noun>

general_pattern = "<#?\w+>"


#Hashtage sign (#) indicates that this variable equals the previous variable.

text = """I don't know who you are. I don't know what you want.
If you are looking for <noun>, I can tell you I don't have money.
But what I do have are a very particular set of <plural>, <#plural> I have acquired over a very long career.
<#plural> that make me a <noun> for people like you. If you let my <noun> go now, that'll be the end of it.
I will not <verb> for you, I will not pursue you.
But if you don't, I will <#verb> for you, I will find you, and I will <verb> you."""


def main():
	global general_pattern, text

	# lambda function to remove <, > and # from the string to present it.

	cleanup = lambda x: x.replace('<', '').replace('>', '').replace('#', '')

	# Get the variables list of the text

	replace_list = re.findall(general_pattern, text)

	for index, value in enumerate(replace_list):
		
		# If it starts with #, follow the last input and continue

		if value.startswith("<#"):

			replace_list[index] = replace_list[index - 1]
			text = text.replace(value, replace_list[index], 1)
			continue


		# Else:

		while True:
			user_input = input("Enter {}: ".format(cleanup(value)))

			if not user_input: continue

			replace_list[index] = Fore.MAGENTA+ user_input +Fore.RESET
			text = text.replace(value, replace_list[index], 1)

			break

	print("\nThe final text is:\n\n" + text + "\n")

if __name__ == '__main__':
	main()