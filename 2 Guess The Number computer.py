IT Guess the Number hack code

Copy and paste from below (do not include this):
import random
#Sets guesses as 1, so I don't add another line of code on the first guess
guesses = 1

#question variable is unneccessary, but a great addition
question = input("Would you like to play Guess the Number? ")
#This simply adds a blank line. Must nicer on the eyes
print("")
if question == "Yes" or question == "yes":
	print("Great choice!")
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
	l = low

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
	h = high

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

u = int(((h - l) / 2) + l)
print("")

#While True loops go on forever unless broken
while True:
	#This is if the guess is correct
	if n == u:
		print(f"{u} is correct! Congratulations!")
		#break is so that it doesn't infinitely print win message
		break
	#If user guess is smaller than the number
	elif u > n:
		h = u
		u = int(((h - l) / 2) + l)
		#Adds to the total guesses
		guesses = guesses + 1
	elif u < n:
		l = u
		u = int(((h - l) / 2) + l)
		guesses = guesses + 1
	#It should be impossible to reach this, as every value must be smaller, equal, or greater than another number
	#I added this anyway just in case, more as a check
	else:
		print("Not sure what happened...")

print("")
#The final amount of guesses. Unnecessary but nice addition.
print(f"It took you {guesses} guesses!")
