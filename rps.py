# Henry Liu
# Rock Paper Scissors
# VARIABLES
import random
pScore = 0
cScore = 0
ties = 0
computerChoices = ["r", "p", "s"]





# Welcome Message
# Print the message
print("Welcome to Rock Paper Scissors") 
# Prompt for player name
pName = input("What is your name? ")



# Final Score
def printScore():
	# Write message
	print("The score is ")
	# Write player score
	print(pName + ": " + str(pScore))
	# Write compute score
	print("Computer: " + str(cScore))
	# Write how many ties
	print("Ties: " + str(ties))

# Game Loop
# make a forever loop
while True:
	# Print current score
	printScore()
	# Prompt for a choice (r (rock), p (paper), s (scissors), q (quit))
	pChoice = input("Enter r (rock), p (paper), s (scissors or q (to quit): ")
	# deal with player entering q
	if pChoice == "q":
		break
	# get computer choice (random)
	cChoice = random.choice(computerChoices)
	# compare for player entering r
	if pChoice == "r":
		print(pName + " picked Rock")
		# if computer is r
		if cChoice == "r":
			print("Computer picked Rock")
			print("This is a tie")
			ties = ties + 1
		# if computer is p
		elif cChoice == "p":
			print("Computer picked Paper")
			print("Paper covers Rock")
			cScore = cScore + 1
		# if computer is s
		else: 
			print("Computer picked Scissors")
			print("Rock breaks Scissors")
			pScore = pScore + 1


	# compare for player entering p
	elif pChoice == "p":
		print(pName + " picked Paper")
		# if computer is r
		if cChoice == "r":
			print("Computer picked Rock")
			print("Paper covers Rock")
			pScore = pScore + 1
		# if computer is p
		elif cChoice == "p":
			print("Computer picked Paper")
			print("This is a tie")
			ties = ties + 1
		# if computer is s
		else: 
			print("Computer picked Scissors")
			print("Scissors cuts paper")
			cScore = cScore + 1

	# compare for player entering s
	elif pChoice == "s":
		print(pName + " picked Scissors")
		# if computer is r
		if cChoice == "r":
			print("Computer picked Rock")
			print("Rock breaks Scissors")
			cScore = cScore + 1
		# if computer is p
		elif cChoice == "p":
			print("Computer picked Paper")
			print("Scissors cuts Paper")
			pScore = pScore + 1
		# if computer is s
		else: 
			print("Computer picked Scissors")
			print("This is a tie")
			ties = ties + 1
	# deal with player entering anything else