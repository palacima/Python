import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import random

board = Series([" "] * 9, index = ['A1','A2','A3','B1','B2','B3','C1','C2','C3'])


# Restarts or Closes the game (depending on user's wants) after someone wins
def end_game():
	print "The Game is Over!"
	global board
	board = Series([" "] * 9, index = ['A1','A2','A3','B1','B2','B3','C1','C2','C3'])
	print "\nPlay again?"
	play_again()
	

def play_again():
	again = raw_input("")
		
	if again.upper() == "YES":
		print "Ok here we go!"
		display_board()
	elif again.upper() == "NO":
		print "Ok, goodbye!"
		quit()
	else:
		print "Please input Yes or No."
		play_again()
			
	
		

# Contains all possible winning combinations for X and O		
def winner():
	if board['A1'] == 'X' and board['A2'] == 'X' and board['A3'] == 'X':
		print "X WINS!!"
		end_game()
	elif board['B1'] == 'X' and board['B2'] == 'X' and board['B3'] == 'X':
		print "X WINS!!"
		end_game()
	elif board['C1'] == 'X' and board['C2'] == 'X' and board['C3'] == 'X':
		print "X WINS!!"
		end_game()
	elif board['A1'] == 'X' and board['B1'] == 'X' and board['C1'] == 'X':
		print "X WINS!!"
		end_game()
	elif board['A2'] == 'X' and board['B2'] == 'X' and board['C2'] == 'X':
		print "X WINS!!"
		end_game()
	elif board['A3'] == 'X' and board['B3'] == 'X' and board['C3'] == 'X':
		print "X WINS!!"
		end_game()
	elif board['A1'] == 'X' and board['B2'] == 'X' and board['C3'] == 'X':
		print "X WINS!!"
		end_game()
	elif board['C1'] == 'X' and board['B2'] == 'X' and board['A3'] == 'X':
		print "X WINS!!"
		end_game()
	elif board['A1'] == 'O' and board['A2'] == 'O' and board['A3'] == 'O':
		print "O WINS!!"
		end_game()
	elif board['B1'] == 'O' and board['B2'] == 'O' and board['B3'] == 'O':
		print "O WINS!!"
		end_game()
	elif board['C1'] == 'O' and board['C2'] == 'O' and board['C3'] == 'O':
		print "O WINS!!"
		end_game()
	elif board['A1'] == 'O' and board['B1'] == 'O' and board['C1'] == 'O':
		print "O WINS!!"
		end_game()
	elif board['A2'] == 'O' and board['B2'] == 'O' and board['C2'] == 'O':
		print "O WINS!!"
		end_game()
	elif board['A3'] == 'O' and board['B3'] == 'O' and board['C3'] == 'O':
		print "O WINS!!"
		end_game()
	elif board['A1'] == 'O' and board['B2'] == 'O' and board['C3'] == 'O':
		print "O WINS!!"
		end_game()
	elif board['C1'] == 'O' and board['B2'] == 'O' and board['A3'] == 'O':
		print "O WINS!!"
		end_game()
	else:
		pass

# Places X on the board depending if the spot is open or not
def place_x():
	display_board()
	print "Where does X go?"
	move = raw_input("")
	if move.upper() == 'A1':
		if board['A1'] == ' ':
			board['A1'] = 'X'
		else:
			print "\nThat spot is taken!"
			place_x()
	elif move.upper() == 'A2':
		if board['A2'] == ' ':
			board['A2'] = 'X'
		else:
			print "\nThat spot is taken!"
			place_x()
	elif move.upper() == 'A3':
		if board['A3'] == ' ':
			board['A3'] = 'X'
		else:
			print "\nThat spot is taken!"
			place_x()
	elif move.upper() == 'B1':
		if board['B1'] == ' ':
			board['B1'] = 'X'
		else:
			print "\nThat spot is taken!"
			place_x()	
	elif move.upper() == 'B2':
		if board['B2'] == ' ':
			board['B2'] = 'X'
		else:
			print "\nThat spot is taken!"
			place_x()
	elif move.upper() == 'B3':
		if board['B3'] == ' ':
			board['B3'] = 'X'
		else:
			print "\nThat spot is taken!"
			place_x()	
	elif move.upper() == 'C1':
		if board['C1'] == ' ':
			board['C1'] = 'X'
		else:
			print "\nThat spot is taken!"
			place_x()	
	elif move.upper() == 'C2':
		if board['C2'] == ' ':
			board['C2'] = 'X'
		else:
			print "\nThat spot is taken!"
			place_x()
	elif move.upper() == 'C3':
		if board['C3'] == ' ':
			board['C3'] = 'X'
		else:
			print "\nThat spot is taken!"
			place_x()
	else:
		print "Not a space"
		place_x()
		
	winner()
	full_board_check(board)		
	place_o()

# Places O on the board depending if the spot is open or not
def place_o():
	display_board()
	print "Where does O go?"
	move = raw_input("")
	if move.upper() == 'A1':
		if board['A1'] == ' ':
			board['A1'] = 'O'
		else:
			print "\nThat spot is taken!"
			place_x()
	elif move.upper() == 'A2':
		if board['A2'] == ' ':
			board['A2'] = 'O'
		else:
			print "\nThat spot is taken!"
			place_x()
	elif move.upper() == 'A3':
		if board['A3'] == ' ':
			board['A3'] = 'O'
		else:
			print "\nThat spot is taken!"
			place_x()
	elif move.upper() == 'B1':
		if board['B1'] == ' ':
			board['B1'] = 'O'
		else:
			print "\nThat spot is taken!"
			place_x()	
	elif move.upper() == 'B2':
		if board['B2'] == ' ':
			board['B2'] = 'O'
		else:
			print "\nThat spot is taken!"
			place_x()	
	elif move.upper() == 'B3':
		if board['B3'] == ' ':
			board['B3'] = 'O'
		else:
			print "\nThat spot is taken!"
			place_x()	
	elif move.upper() == 'C1':
		if board['C1'] == ' ':
			board['C1'] = 'O'
		else:
			print "\nThat spot is taken!"
			place_x()	
	elif move.upper() == 'C2':
		if board['C2'] == ' ':
			board['C2'] = 'O'
		else:
			print "\nThat spot is taken!"
			place_x()
	elif move.upper() == 'C3':
		if board['C3'] == ' ':
			board['C3'] = 'O'
		else:
			print "\nThat spot is taken!"
			place_x()
	else:
		print "Not a space"
		place_o()	
		
	winner()
	full_board_check(board)
	place_x()

# Determines who goes first
def first_move():
	num = random.randint(1,100)
	
	while True:
		try:
			xans = int(raw_input("Player X, pick a number between 1 and 100."))
			xdiff = abs(num - xans)
		except:
			print "Pick a number this time!"
			continue
		else:
			break
	while True:
		try:
			oans = int(raw_input("Player O, pick a number between 1 and 100."))
			odiff = abs(num - oans)
		except:
			print "Pick a number this time!"
			continue
		else:
			break
	
	if xdiff < odiff:
		print "The number was %s!" % num
		print "X goes first!"
		place_x()
	elif odiff < xdiff:
		print "The number was %s!" % num
		print "O goes first!"
		place_o()
	else:
		print "\nYou both are closest! Let's guess again!"
		first_move()

def full_board_check(board):
	if board['A1'] != ' 'and \
		board['A2'] != ' ' and \
		board['A3'] != ' ' and \
		board['B1'] != ' ' and \
		board['B2'] != ' ' and \
		board['B3'] != ' ' and \
		board['C1'] != ' ' and \
		board['C2'] != ' ' and \
		board['C3'] != ' ':
		print "It's a tie!"
		end_game()
	else:
		pass
		
def play_game():
	play = raw_input("Play game? ")
	if play.upper() == "YES":
		first_move()
	elif play.upper() == "NO":
		print "Ok goodbye!"
		quit()	
	else:
		print "Please write yes or no."
		play_game()

# Shows the set up of the board and updates move by move
def display_board():
	print "\nThis is the current board: \n"
	print "A|   " + board['A1'] + "  | " + board['A2'] + "  | " + board['A3'] + " "
	print "    --------------"
	print "B|   " + board['B1'] + "  | " + board['B2'] + "  | " + board['B3'] + " "
	print "    --------------"
	print "C|   " + board['C1'] + "  | " + board['C2'] + "  | " + board['C3'] + " " 
	print "     " + " 1  " + "  2  " + "  3"

play_game()