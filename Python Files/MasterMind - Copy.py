import random

def lets_begin():
    print ("Welcome to the Mastermind Game!")
    return
 
# Display Menu
print (" ---------------------------")
print ("     The MASTERMIND Game    ")
print (" ---------------------------")
print ("Guess the secret color code in as few tries as possible.\n")
print ("Please, enter your color code.")
print ("You can use R - Red, G - Green, B - Blue, Y - Yellow, W - White and O - Orange")
print ("Example of a color code : RGBY")


# List of Colors
colors = ["R", "G", "B", "Y", "W", "O"]
attempts = 0
game = True

# System randomwly generates four-color code
color_code = random.sample(colors,4)


# player guesses the code(while loop)	
while game:
	correct_color = ""
	guessed_color = ""
	player_guess = input().upper()
	attempts += 1
	
# determine if the player's input is correct
	if len(player_guess) != len(color_code):
		print ("\nError! The secret code has exactly four colors. Please enter four color codes!")
		continue
	for i in range(4):
		if player_guess[i] not in colors:
			print ("\nError! Unknown color code! Refer above for the color codes list")
			continue
			
# comparing player's input code and the secret code
	if correct_color != "OOOO":
		for i in range(4):
			if player_guess[i] == color_code[i]:
				correct_color += "O"
			if  player_guess[i] != color_code[i] and player_guess[i] in color_code:
				guessed_color += "X"
		print (correct_color +  guessed_color + "\n")		
		
	if correct_color == "OOOO":
		if attempts == 1:
			print ("Amazing!! You guessed it correctly on first try!")
		else:
			print ("Good job! You took " + str(attempts) + " tries to guess.")
		game = False
		
	if attempts >= 1 and attempts <6 and correct_color != "OOOO":
		print ("Next attempt: ")
	elif attempts >= 6:
		print ("You didn't guess the color code right. The secret color code was: " + str(color_code))
		print ("Please enter the given code to restart the game")

# continue playing or stop playing
	while game == False:
		finish_game = input("Would you like to play again (Y/N)?").upper()	
		attempts = 0
		if finish_game =="N":
			print ("Thank you for playing! Goodbye!")
		elif finish_game == "Y":
			game = True
			print ("That was fun! Let's play again...")
		

                                
                                

