import random

guesses = 10
words = ["hello", "there", "general"]
n = random.choice(words)
display = "*" * len(n)

print("")
print(f"Welcome to Hangman. If you don't know how to play, there is a mystery word and you must guess letter by letter. Be careful, you only have {guesses} guesses!")
print("")

while guesses >= 1:
	u = input("Guess a letter: ")
	print("")
	
	while u.isalpha() == False:
		u = input("Please choose a letter: ")
		print("")
	
	u_lower = u.lower()
	
	if u_lower in n:
		print("Great guess!")
		print("")
		new_display = ''
		for w, l in zip(n, display):
			if u_lower == w:
				new_display += u_lower
			else:
				new_display += l
		display = new_display
		print(display)
		print("")
		if not '*' in display:
			print("You won!")
			break	
	else:
		print("Incorrect")
		print("")
		guesses = guesses - 1
		if guesses != 1 and guesses != 0:
			print(f"You've got {guesses} guesses left")
		if guesses == 1:
			print(f"You've got {guesses} guess left")
		if guesses == 0:
			print("Oh no! You've run out of guesses! Better luck next time!")
		print("")
		
