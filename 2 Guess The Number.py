import random

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
		print("")
		#break is so that it doesn't infinitely print win message
		break
		

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
