from sys import exit
import random
def gold_room():
	print "\n This room is full of gold. How much do you take?"

	choice = raw_input("> ")
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You are greedy bastard!")

def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		choice = raw_input("> ")

		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."

def dragon_room():
	print "\n Here you see the great evil flying Dragon."
	print "\n He, it, whatever stares at you and you go insane."
	print "\n What you'll do now?"
	print "\n Throw something at the Dragon?"
	print "\t (Target the Eye, if you miss it then dragon will eat you up!)"
	print "\n Or maybe try to be friend with the dragon!"
	print "\t (Might accept or eat you up!)"
	print "\nThrow or Friend?"

	choice = raw_input("\n> ")

	a = bool(random.choice([True,False]))

	if "throw" in choice:
		if a == True:
			print "\n Good Shot! Dragon down!"
			print "\n You entered a new room now"
			gold_room()
		elif a == False:
			print "\n Ouch! Missed the target!"
			dead("\n Dragon eats you up!")

	elif "friend" in choice:
		if a == True:
			print "\n Well Done!"
			print "\n You've got a brand new Friend!"
			print "\n Now you entered a new room"
			gold_room()
		elif a == False:
			print "\n Oops! Dragon not so friendly!"
			dead("\n Dragon eats you up!")

	else:
		def get_choice(choices):
			choice = ""
			while choice not in choices:
				choice = raw_input("\n Choose one of [%s]: " %", ".join(choices))
			return choice
		choice = get_choice(["friend","throw"])
		print choice

		print "I got no idea what that means."

def dead(why):
	print why, "Good job!\n "
	exit(0)

def start():
	print "\n You are in a dark room."
	print "\n There is a door to your right and left."
	print "\n Which one do you take?"

	choice = raw_input("\n > ")

	if choice == "left":
		bear_room()
	elif choice == "right":
		dragon_room()
	else:
		dead("You stumble around the room until you starve.")

if __name__ == "__main__":
	start()
