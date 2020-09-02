import random
import sys

sys.setrecursionlimit(25000) # sometimes ther's a recursion error, so...

board = [' ' for x in range(26)] # create the board spaces


def print_board(board):
	print(board[1], ' |', board[2], ' |', board[3], ' |', board[4], ' |', board[5])
	print('--', '+', '--', '+', '--', '+', '--', '+', '--')
	print(board[6], ' |', board[7], ' |', board[8], ' |', board[9], ' |', board[10])
	print('--', '+', '--', '+', '--', '+', '--', '+', '--')
	print(board[11], ' |', board[12], ' |', board[13], ' |', board[14], ' |', board[15])
	print('--', '+', '--', '+', '--', '+', '--', '+', '--')
	print(board[16], ' |', board[17], ' |', board[18], ' |', board[19], ' |', board[20])
	print('--', '+', '--', '+', '--', '+', '--', '+', '--')
	print(board[21], ' |', board[22], ' |', board[23], ' |', board[24], ' |', board[25])

def full_board(): # check if the board is full
	if board.count(' ') > 1:
		return
	else:
		print("It's a tie")
		quit()

def check_win(bo, le): #check all the options and if there's a win the game ends (bo = board, le = letter)
	if (bo[1] == le and bo[2] == le and bo[3] == le and bo[4] == le and bo[5] == le) or (bo[6] ==le and bo[7] == le and bo[8] == le and bo[9] == le and bo[10] == le) or (bo[11] ==le and bo[12] == le and bo[13] == le and bo[14] == le and bo[15] == le) or (bo[16] ==le and bo[17] == le and bo[18] == le and bo[19] == le and bo[20] == le) or (bo[21] ==le and bo[22] == le and bo[23] == le and bo[24] == le and bo[25] == le) or (bo[1] == le and bo[6] == le and bo[11] == le and bo[16] == le and bo[21] == le) or (bo[2] == le and bo[7] == le and bo[12] == le and bo[17] == le and bo[22] == le) or (bo[3] ==le and bo[8] == le and bo[13] == le and bo[18] == le and bo[23] == le) or (bo[4] ==le and bo[9] == le and bo[14] == le and bo[19] == le and bo[24] == le) or (bo[5] ==le and bo[10] == le and bo[15] == le and bo[20] == le and bo[25] == le) or (bo[1] ==le and bo[7] == le and bo[13] == le and bo[19] == le and bo[25] == le) or (bo[5] ==le and bo[9] == le and bo[13] == le and bo[17] == le and bo[21] == le):
		print("Has won the ", le, "'s")
		quit()
	else:
		return

def check_win2(bo, le): # this is like the last one but with little different output. Is used for the AI function
						# to check if the computer or the player can win with a single move
	return (bo[1] == le and bo[2] == le and bo[3] == le and bo[4] == le and bo[5] == le) or (bo[6] ==le and bo[7] == le and bo[8] == le and bo[9] == le and bo[10] == le) or (bo[11] ==le and bo[12] == le and bo[13] == le and bo[14] == le and bo[15] == le) or (bo[16] ==le and bo[17] == le and bo[18] == le and bo[19] == le and bo[20] == le) or (bo[21] ==le and bo[22] == le and bo[23] == le and bo[24] == le and bo[25] == le) or (bo[1] == le and bo[6] == le and bo[11] == le and bo[16] == le and bo[21] == le) or (bo[2] == le and bo[7] == le and bo[12] == le and bo[17] == le and bo[22] == le) or (bo[3] ==le and bo[8] == le and bo[13] == le and bo[18] == le and bo[23] == le) or (bo[4] ==le and bo[9] == le and bo[14] == le and bo[19] == le and bo[24] == le) or (bo[5] ==le and bo[10] == le and bo[15] == le and bo[20] == le and bo[25] == le) or (bo[1] ==le and bo[7] == le and bo[13] == le and bo[19] == le and bo[25] == le) or (bo[5] ==le and bo[9] == le and bo[13] == le and bo[17] == le and bo[21] == le)

def player_move(move, which_game):	# execute the player move

	if board[move] == ' ' and move >= 1 and move <= 25:
		board[move] = 'x'
		return move
	else:
		print('Invalid move')
		if which_game == 'ai':
			main2()
		elif which_game == 'random':
			main()


def pc_move(move): # this is the computer move, it choses a position ramdomly
	move = random.randrange(1, 26)
	if board[move] == ' ':
		board[move] =  'o'
		return move
	else:
		full_board()
		pc_move(move)

def ai(move): # this is how the AI chooses its move.
	
	# 1. check if the computer can win with a single movement
	# 2. whith the same code, check if the player can win with a move
	possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0] 
	move = 0
	for let in ['o','x']:
		for i in possibleMoves:
			boardCopy = board[:]
			boardCopy[i] = let
			if check_win2(boardCopy, let):
				move = i
				board[i] = 'o'
				return move

	# 3. the same as before but with 2 moves
	for let in ['o','x']:
		for i in possibleMoves:
			for j in possibleMoves:
				boardCopy = board[:]
				boardCopy[i] = let
				boardCopy[j] = let
				if check_win2(boardCopy, let):
					move = i
					board[i] = 'o'
					return move

	# 4. check if the middle is empty, if it is chose that.
	if board[13] == ' ':
		board[13] = 'o'
		move = 13
		return move

	# 5. same as step 3 but with 3 moves
	for let in ['o','x']:
		for i in possibleMoves:
			for j in possibleMoves:
				for t in possibleMoves:
					boardCopy = board[:]
					boardCopy[i] = let
					boardCopy[j] = let
					boardCopy[t] = let
					if check_win2(boardCopy, let):
						move = i
						board[i] = 'o'
						return move

	pc_move(move)


def main():     # the main function for the easy verson of the game

	check_win(board, 'x')
	check_win(board, 'o')
	full_board()
	try:
		move = int(input("At which position do you move? 1-25   "))
	except ValueError:
		print("Invalid input. Please enter an integer number\n")
		main()
	
	if move >= 1 and move <= 25:
		pass
	else:
		print('Invalid position')
		main()

	player_move(move, 'random')
	print_board(board)
	print("\n")
	pc_move(move)
	print_board(board)
	print("\n")

	main()

def main2():    # the main function for the hard version of the game

	check_win(board, 'x')
	check_win(board, 'o')
	full_board()
	try:
		move = int(input("At which position do you move? 1-25   "))
	except ValueError:
		print("Invalid input. Please enter an integer number\n")
		main2()

	if move >= 1 and move <= 25:
		pass
	else:
		print('Invalid position')
		main2()
	player_move(move, 'ai')
	print_board(board)
	print("\n")
	ai(move)
	print_board(board)
	print("\n")

	main2()

def version():  # chose a version of the game
	try: 
		version1 = str(input("Do you want to play the easy or hard version? (e/h)   "))
	except ValueError:
		print("Invalid input, please enter just e or h")
		version()

	if version1.lower() == 'e':
		main()
	elif version1.lower() == 'h':
		main2()
	else:
		print('Error')
		version()

version()