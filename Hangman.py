import os
def get_word():
	wrong = 0 
	turns = 10
	chosenWord = "to kill a mockingbird"
	
	board = ["_"] * len(chosenWord)
	print(board)
	win = False
	print("Hangman starting!!!")
	while turns > 0:
		print("\n")
		msg = "Guess a letter"
		letter = input(msg)
		turns -= 1
		if letter in chosenWord:
			print(letter)
			
			
		else:
			wrong += 1
			print("-")
		
		e = wrong + 1
		
		if "_" not in board:
			print("Winner!")
			
			win = True
			break
get_word()	
