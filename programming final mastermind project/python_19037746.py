import random

def lets_begin(text):
    print (text)
    return
lets_begin("Welcome to the Mastermind Game!")

 
# Display Menu
print (" ---------------------------")
print ("     The MASTERMIND Game    ")
print (" ---------------------------")
print ("Guess the secret color code in as few tries as possible.\n")
print ("Please, enter your color code.")
print ("You can use R - Red, G - Green, B - Blue, Y - Yellow, W - White and O - Orange")
print ("Example of a color code : RGBY")
print ("Please use all uppercase letters")


# List of Colors
colors = ["R", "G", "B", "Y", "W", "O"]
attempts = 0
game = True

# System randomwly generates four-color code
passcode = random.sample(colors,4)


# player guesses the code(while loop)	
while game:
	generated_color = ""
	guesses = ""
	users_guess = input()
	attempts += 1
	
# determine if the player's input is correct
	if len(users_guess) != len(passcode):
		print ("Error! The secret code has exactly four colors. Please enter four color codes!")
		continue
	for i in range(4):
		if users_guess[i] not in colors:
			print ("Error! Unknown color code! Refer above for the color codes list")
			continue
			
# comparing player's input code and the secret code
	if generated_color != "OOOO":
		for i in range(4):
			if users_guess[i] == passcode[i]:
				generated_color += "O"
			if users_guess[i] != passcode[i] and users_guess[i] in passcode:
				guesses += "X"
		print (generated_color +  guesses)		
		
	if generated_color == "OOOO":
		if attempts == 1:
			print ("Amazing!! You guessed it correctly on first try!")
		else:
			print ("Good job! You took " + str(attempts) + " tries to guess.")
		game = False
		
	if attempts >= 1 and attempts <4 and generated_color != "OOOO":
		print ("Try again: ")
	elif attempts >= 4:
		print ("You didn't guess the color code right. The secret color code was: " + str(passcode))
		print ("Please enter the given code to restart the game")

# continue playing or stop playing
	while game == False:
		finish_game = input("Would you like to play again (Y/N)?")	
		attempts = 0
		if finish_game =="N":
			print ("Thank you for playing! Goodbye!")
		elif finish_game == "Y":
			game = True
			print ("That was fun! Let's play again...")
			print ("Guess the secret color code in as few tries as possible.\n")
			print ("Please, enter your color code.")
			print ("You can use R - Red, G - Green, B - Blue, Y - Yellow, W - White and O - Orange")
			print ("Example of a color code : RGBY")
			
# Arranged by Chew Chien Zhen
