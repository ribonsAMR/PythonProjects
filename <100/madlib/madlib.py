import re
from colorama import init, Fore
init(autoreset=True)

general_pattern = "<#?\w+>" # <noun> <#noun>

text = """I don't know who you are. I don't know what you want.\nIf you are looking for <noun>, I can tell you I don't have money.\nBut what I do have are a very particular set of <plural>, <#plural> I have acquired over a very long career.\n<#plural> that make me a <noun> for people like you. If you let my <noun> go now, that'll be the end of it.\nI will not <verb> for you, I will not pursue you.\nBut if you don't, I will <#verb> for you, I will find you, and I will <verb> you."""

replace_list = re.findall(general_pattern, text)

for index, value in enumerate(replace_list):
	if value.startswith("<#"):
		replace_list[index] = replace_list[index - 1]
		text = text.replace(value, replace_list[index], 1)
		continue

	while True:
		user_input = input("Enter {}: ".format(value))

		if not user_input: continue

		replace_list[index] = Fore.MAGENTA+ user_input +Fore.RESET
		text = text.replace(value, replace_list[index], 1)

		break

print(text)