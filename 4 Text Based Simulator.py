#Please choose a code from one of the files (on the left)
#Text Based Adventure Game

import time

#Variables
#rooms
room_1 = 1
room_2 = 0
room_3 = 0
#inputs
action = 0
start = 0
#tools
key = 0
screwdriver = 0
sword = 0
food = 0
#endings
win = 0
death = 0

print("Welcome to Text-Based Adventure Game!")
print("")
time.sleep(1)
print("In this game your objective is to escape, and most importantly, survive.")
print("")
time.sleep(1)
while start != "y" or start != "n":
	start = input("Would you like to start (y/n)? ")
	print("")
	if start == "y":
		print("Great, let's begin!")
		break
	elif start == "n":
		print("That's a shame...")
	else:
		print("Please type y (yes) or n (no).")
print("")
time.sleep(1)
print("In this game, you must give one-word answers (without any capitals).")
print("")
time.sleep(1)
print("Good luck!")
for x in range(5):
	print("")
time.sleep(1)

#room 1
print("You wake up in a room. No windows. No natural light. Just a lantern beside you. Or at least that's what your morning haze reported. You stumble out of that creaky bed, and into the centre of the room. Seems to be a single step either direction, small room...")
print("")
time.sleep(3)
print("You look towards the East and see a wardrobe. Toward the South there is your bed. In the West there is a cabinet. And in front of you in the North, there is the door.")
print("")
time.sleep(2)
while room_1 == 1:
	action = input("What do you check? ")
	print("")
	if action == "door" and key == 0:
		print("Damn, the handle won't budge. But it seems to have a key hole...")
	elif action == "door" and key == 1:
		print("Hazaah! The key worked! Into the abyss!")
		key = 0
		action = 0
		room_1 = 0
		room_2 = 1
	elif action == "cabinet":
		print("There wasn't much, but there was a key...")
		key = 1
	elif action == "bed":
		print("As expected there wasn't much. But there was a pillow and sheets?")
	elif action == "wardrobe":
		print("It was surprisingly empty...")
	elif action == "keyhole":
		print("Can't see much. Looks like the only true way to get an answer is to walk through that door...")
	else:
		print("Sadly that can't be checked")
	print("")
	time.sleep(1)
for x in range(5):
	print("")

#room 2
print("You arrive on the other side of the door, but sadly you're not free yet. You notice that this room is a little different from the last. It seemed more living room-y. A couch sat on your left in the West. There was a coffee table on your right in the East. The door you passed through behind you in the South. But, nothing in front. How are you supposed to get out!?")
print("")
time.sleep(5)
print("But this time it wasn't just a lantern giving light, but there was a sliver of light coming through a vent above the coffee table on the right. This might be it! But just as quick as you thought it, you couldn't help but think what kind of sick game this is...")
print("")
time.sleep(5)
while room_2 == 1:
	action = input("What do you check? ")
	print("")
	if action == "coffee table" or action == "coffee" or action == "table":
		print("Considering it was a coffee table, it wasn't odd that there was only a cup mat. Nothing else to report here.")
	elif action == "couch":
		print("Seems like someone lost a couple coins to this couch over the years. But... wait what? Why is there a screw driver here?! Seems like someone really went out of their way to hide it...")
		screwdriver = 1
	elif action == "door":
		print("Seems as if it locked you out. Must be one way...")
	elif action == "vent" and screwdriver == 0:
		print("The light is blinding. As for getting through? The vent won't move! Clearly fingers and nails won't do anything to those screws. If only you had a screwdriver...")
	elif action == "vent" and screwdriver == 1:
		print("It... worked! Suprising, right? Anyway, time to crawl to victory!")
		action = 0
		screwdriver = 0
		room_3 = 1
		room_2 = 0
	else:
		print("Sadly that can't be checked")
	print("")
	time.sleep(1)
for x in range(5):
	print("")

#room 3
print("You've crawled through that oddly clean and web-free vent, and found yourself in a cave? You are clearly surprised, as that certainly was not expected. But nonetheless, here you are.")
print("")
time.sleep(3)
print("You search around the small cave area with caution. You find a sleeping giant enemy spider in the North in front of you blocking a small rock corridor, a sword to your left in the West, some (presumably spider) food to your right in the East, and in the South you find nothing. Just a wall.")
print("")
time.sleep(5)
while room_3 == 1:
	action = input("What do you check? ")
	print("")
	if action == "spider" and sword == 0 and food == 0:
		print("You attacked the spider with furiosity. Sadly, your hands did nothing. Despite the spider being asleep, you were still no match. What a shame. As you could imagine, you died. What a shame.")
		death = 1
		room_3 = 0
	elif action == "spider" and sword == 1 and food == 0:
		print("You charged at the spider with the loudest battlecry ever heard. The following battle was epic, the swing of the sword and the... whatever spiders do. Despite your enthusiasm and heroicness, it did not turn out to be. On your finishing strike, the spider got the upper hand. You died. Upon reflection, maybe you should have used that food somehow.")
		death = 1
		room_3 = 0
	elif action == "spider" and sword == 1 and food == 1:
		print("You barrel towards the spider, face full of confidence. Your scream was inaudible from the pure decibels you mustered. The spider quickly got into its battle stance, but it couldn't resist your spider food. Distracted, the spider was doomed from your expertise with the sword. The battle was enough to rewrite history as you knew it. Your skill overcame the spider swiftly, putting down the beast.")
		print("")
		print("Thanks to your outstanding victory, you strolled through the following hallway unopposed. You head towards the light...")
		sword = 0
		food = 0
		room_3 = 0
		win = 1
		time.sleep(1)
	elif action == "hallway":
		print("You carefully tiptoe your way towards the hallway, cautious not to wake the spider. Whilst you go over its third leg, it began to stir. You quickly run straight back where you came from. As you glance over your shoulder, you see that it has once again gone to sleep. Clearly you'll have to deal with the spider first...")
	elif action == "sword":
		print("You move toward the sword. It looks... mighty. Certainly felt like it when you picked it up. I bet you could defeat (nearly) any foe with this...")
		sword = 1
	elif action == "food" or action == "(presumably spider) food":
		print("As you approach the food, it began to move. Not all of it, just a lot. As you look closer, you saw worms! Ew! Anyway, you clearly hate it, but maybe the spider won't?")
		food = 1
	elif action == "wall" or action == "south":
		print("You turn around and gasp at what you found, a wall! What did you expect. I told you it was a wall.")
	else:
		print("Unfortunately, that can't be checked.")
	print("")
	time.sleep(1)
for x in range(5):
	print("")

#ending
if win == 1:
	print("The light is overwhelming. The contrast between the dim light of the lanterns and caves compared between the sun is unfathomable. You are blinded for numerous seconds, as your eyes adjust. Upon your vision returning, you find the open world. Freedom! The great vastness of the world. Free at last!")
elif death == 1:
	print("Real shame that you died. Want to try again? If so, click 'Stop' up the top, then click 'Run' again.")
