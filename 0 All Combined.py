import random
play = 1
while play == 1:
	choice = 1
	while choice == 1:
		dice = 0
		guess = 0
		mad = 0
		hang = 0
		
		print("Which game do you want to play?")
		print("")
		print("Type 'a' for Dice Rolling Simulator")
		print("Type 'b' for Guess the Number")
		print("Type 'c' for Mad Libs Generator")
		print("Type 'e' for Hangman")
		print("")
		game = input("So, what is it going to be? ")
		print("")
		if game == 'a':
			print("Dice Rolling Simulator, great choice!")
			choice = 0
			dice = 1
			for x in range(15):
				print("")
		elif game == 'b':
			print("Guess the Number, great choice!")
			choice = 0
			guess = 1
			for x in range(15):
				print("")
		elif game == 'c':
			print("Mad Libs Generator, great choice!")
			choice = 0
			mad = 1
			for x in range(15):
				print("")
		elif game == 'e':
			print("Hangman, great choice!")
			choice = 0
			hang = 1
			for x in range(15):
				print("")
		else:
			print("Are you going to choose one, or not? ")
			print("")

	
	
	
	
	
	
	while dice == 1:
		print("Welcome to Dice Rolling Simulator!")
		print("")
		#I have annotated the code so you can understand my thought process
		#There are also a lot of outcomes, make sure to check them all!
	
		#decision variable determines whether to roll the die
		decision = input("Would you like to make and roll a die? ")
		#this simply gives a break between lines, much nicer on the eyes
		print("")
		#checks two answers: "Yes" and "yes"
		if decision == "Yes" or decision == "yes" or decision == "y":
			print("Correct choice!")
		elif decision == "No" or decision == "no" or decision == "n":
			print("Bad choice, you will have to anyway")
		else:
			print("I'll take it as a yes!")
		print("")
	
		#asking the user allows more variety and enjoyment
		sides = input("How many sides would you like on your die? ")
		print("")
		#usually having int(input... will have an error if the answer is not a digit
		#below allows me to check and change without an error message (smoother for the user)
		while sides.isdigit() == False:
			print("Please choose an integer")
			print("")
			#repeats the question
			sides = input("How many sides would you like on your die? ")
			print("")
		#when sides is a digit, the while loop ends, and becomes an integer
		if sides.isdigit():
			sides = int(sides)
			
		#I've stopped it at 1 (as it is technically possible with a sphere)). If below 2, then the user will be asked again 
		while sides<1:
			print("Please choose an integer above 1")
			print("")
			sides = int(input("How many sides would you like on your die? "))
			print("")
		#Thought I might add in a sly comment
		if sides == 1:
			print("I'm not sure what you're expecting to get out of this...")
			print("")
		
		#Asking allows more choices (and coding)
		roll = input("Would you like to roll the die? ")
		print("")
		if roll == "Yes" or roll == "yes":
			#It randomises between 1 and the amount of sides previously asked
			n = random.randint(1, sides)
			print(f"You have rolled a {n}!")
		elif roll == "No" or roll == "no":
			print("That's alright, I guess...")
			print("")
			rmen = input("Does that mean you would like to restart, go to the main menu, end the program, or do nothing('r', 'm', 'e', or n)? ")
			print("")
			if rmen == "r" or rmen == "restart":
				print("Restart it is!")
				dice = 1
				for x in range(10):
					print("")
				break	
			elif rmen == "m" or rmen == "main" or rmen == "menu" or rmen == "main menu":
				print("Main menu it is!")
				dice = 0
				choice = 1
				for x in range(15):
					print("")
				break						
			elif rmen == 'e' or rmen == "end" or rmen == "end my suffering":
				print("Your suffering has ended")
				for x in range(20):
					print("")
				dice = 0
				play = 0
				break
			elif rmen == 'n' or rmen == 'nothing' or rmen == "do nothing":
				print("Great, let us continue!")
				roll = "continue"
			else:
				rmen = ("Please type either: 'r' for restart, 'm' for main menu, 'e' for end, or 'n' for nothing: ")
		else:
			#This allows me not to code infinite if statements
			print("Please type: Yes or No")
		print("")
		#I've added 'While True' to cause an infinite loop
		while True:
			roll = input("Would you like to roll the die again? ")
			print("")
			if roll == "Yes" or roll == "yes" or roll == "y":
				n = random.randint(1, sides)
				print(f"You have rolled a {n}!")
			elif roll == "No" or roll == "no" or roll == "n":
				print("That's alright, I guess...")
				print("")
				rmen = input("Does that mean you would like to restart, go to the main menu, end the program, or do nothing('r', 'm', 'e', or 'n')? ")
				print("")
				if rmen == "r" or rmen == "restart":
					print("Restart it is!")
					dice = 1
					for x in range(10):
						print("")
					break
					
				elif rmen == "m" or rmen == "main" or rmen == "menu" or rmen == "main menu":
					print("Main menu it is!")
					dice = 0
					choice = 1
					for x in range(15):
						print("")
					break						
				elif rmen == 'e' or rmen == "end" or rmen == "end my suffering":
					print("Your suffering has ended")
					for x in range(20):
						print("")
					dice = 0
					play = 0
					break
				elif rmen == 'n' or rmen == 'nothing' or rmen == "do nothing":
					print("Great, let us continue!")
					roll = "continue"
				else:
					rmen = ("Please type either: 'r' for restart, 'm' for main menu, 'e' for end, or 'n' for nothing: ")
			else:
				print("Please type: Yes or No")
			print("")
	









	while guess == 1:
			print("Welcome to Guess the Number!")
			print("")
			#Sets guesses as 1, so I don't add another line of code on the first guess
			guesses = 1
			
			#question variable is unneccessary, but a great addition
			question = input("Are you excited to play Guess the Number? ")
			#This simply adds a blank line. Must nicer on the eyes
			print("")
			if question == "Yes" or question == "yes":
				print("Great to hear!")
			elif question == "No" or question == "no":
				print("That's a shame... You'll have to play anyway!")
			else:
				print("I'll take that as a yes!")
			print("")

			#This asks the user for the lowest value
			low = input("What would you like the lowest number to be? ")
			print("")
			#Below is so it only int's a digit. This is to avoid an error message
			while low.isdigit() == False:
				print("Please give an integer")
				print("")
				low = input("What would you like the lowest number to be? ")
				print("")
			if low.isdigit():
				low = int(low)
			
			#Asks for the highest value, much like the lowest value
			high = input("What would you like the highest number to be? ")
			print("")
			while high.isdigit() == False:
				print("Please give an integer")
				print("")
				high = input("What would you like the highest number to be? ")
				print("")
			if high.isdigit():
				high = int(high)
			
			#Below is making sure that low is lower than high (to avoid an error message)
			#If not, It asks it reassign high value
			while low > high:
				print(f"Please choose a number higher than {low}")
				print("")
				high = input("What would you like the highest number to be? ")
				print("")
				while high.isdigit() == False:
					print("Please give an integer")
					print("")
					high = input("What would you like the highest number to be? ")
					print("")
				if high.isdigit():
					high = int(high)
					print("")
			
			#This randomises the number
			n = random.randint(low,high)
			#hint is something I added in if I couldn't guess it
			hint = n - 1
			
			u = input("What do you think the number is? ")
			print("")
			
			#Checks that the guess is an integer. If not, retry.
			while u.isdigit() == False:
				print("Please give an integer")
				print("")
				#u is the user's guess
				u = input("What do you think the number is? ")
				print("")
			if u.isdigit():
				u = int(u)
			
			#While True loops go on forever unless broken
			while True:
				#This is if the guess is correct
				if n == u:
					print(f"{u} is correct! Congratulations!")
					#break is so that it doesn't infinitely print win message
					rme = input("Would you like to restart, go to the main menu, or end the program('r', 'm', or 'e')? ")
					print("")
					if rme == "r" or rme == "restart":
						print("Restart it is!")
						guess = 1
						break	
					elif rme == "m" or rme == "main" or rme == "menu" or rme == "main menu":
						print("Main menu it is!")
						guess = 0
						choice = 1
						break						
					elif rme == 'e' or rme == "end" or rme == "end my suffering":
						print("Your suffering has ended")
						for x in range(20):
							print("")
						guess = 0
						play = 0
						break
					else:
						rme = print("Please type either: 'r' for restart, 'm' for main menu, or 'e' for end")
				
				#If user guess is smaller than the number
				elif u > n:
					u = input(f"{u} is too large! Try again: ")
					print("")
					while u.isdigit() == False:
						print("Please give an integer")
						print("")
						u = input("What do you think the number is? ")
						print("")
					if u.isdigit():
						u = int(u)
					#Adds to the total guesses
					guesses = guesses + 1
				elif u < n:
					u = input(f"{u} is too small! Try again: ")
					print("")
					#This is the hint function. Supposed to be a secret
					#You may also notice, only works when user guess is smaller than number. It's intentional.
					if u == "hint":
						print(f"Hint, the answer is greater than {hint}")
						print("")
					while u.isdigit() == False:
						print("Please give an integer")
						print("")
						u = input("What do you think the number is? ")
						print("")
					if u.isdigit():
						u = int(u)
					guesses = guesses + 1
				#It should be impossible to reach this, as every value must be smaller, equal, or greater than another number
				#I added this anyway just in case, more as a check
				else:
					print("Not sure what happened...")
			
			print("")
			#The final amount of guesses. Unnecessary but nice addition.
			print(f"It took you {guesses} guesses!")
			print("")
			for x in range(15):
				print("")

	while hang == 1:
		import random

		guesses = 10
		words = ["hello", "there", "general", "kenobi"]
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
