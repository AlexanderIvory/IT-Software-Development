#I have annotated the code so you can understand my thought process
#There are also a lot of outcomes, make sure to check them all!
import random

#decision variable determines whether to roll the die
decision = input("Would you like to make and roll a die? ")
#this simply gives a break between lines, much nicer on the eyes
print("")
#checks two answers: "Yes" and "yes"
if decision == "Yes" or decision == "yes":
	print("Correct choice!")
elif decision == "No" or decision == "no":
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
	#restart variable is designed if you don't have the amount of sides you wanted
	restart = input("Does that mean you would like to restart? ")
	if restart == "Yes" or restart == "yes":
		print("Then please click 'Stop' and then click 'Run'")
	elif restart == "No" or restart == "no":
		print("Great! Let us continue!")
	else:
		print("Please type either: Yes or No")
else:
	#This allows me not to code infinite if statements
	print("Please type: Yes or No")
print("")
#I've added 'While True' to cause an infinite loop
while True:
	roll = input("Would you like to roll the die again? ")
	print("")
	if roll == "Yes" or roll == "yes":
		n = random.randint(1, sides)
		print(f"You have rolled a {n}!")
	elif roll == "No" or roll == "no":
		print("That's alright, I guess...")
		print("")
		restart = input("Does that mean you would like to restart? ")
		print("")
		if restart == "Yes" or restart == "yes":
			print("Then please click 'Stop' and then click 'Run'")
		elif restart == "No" or restart == "no":
			print("Great! Let us continue!")
		else:
			print("Please type either: Yes or No")
	else:
		print("Please type: Yes or No")
	print("")

