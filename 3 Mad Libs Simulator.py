#Unnecessary, but adds more to the game
question = input("Would you like to play Mad Libs Generator? ")
print("")
#Same as above
if question == "Yes" or question == "yes" or question == "y":
	print("Correct choice!")
elif question == "No" or question == "no" or question == "n":
	print("What a shame... well, you'll have to play anyway!")
else:
	print("I'll take that as a yes!")
print("")

#Explaining the game
print("To play this game, you must choose a couple of different words, and it will turn into a story!")
print("")
	
#Asks for name so we can implement it into the story
name = input("Who is your character? ")
print("")

#Same as above, but for setting
setting = input("Where is the setting? ")
print("")

#Same as above, but for action and used f-strings to make it more engaging
action = input(f"What was {name} doing? ")
print("")

#Same as above but for why they were doing the action. Not necessary but adds more to the story
why = input(f"Why was {name} {action}? ")
print("")

#The story itself. Used f-string to include the the variables.
print(f"Once, there was a particular {name}. {name} was at {setting}. What was {name} doing? Great question. Well, it turns out {name} was {action}. Can you believe it? I know I didn't, until I realised {name} was {action} to {why}.")
