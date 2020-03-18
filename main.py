import Bollywood
import Tic_Tac_Toe
import KMST
import Quiz
import SodukoSolver
"""Initializing the games """
run = False
print('// WELCOME TO INDIAN BOARD GAMES // ')
games = [Bollywood.Bollywood,Tic_Tac_Toe.Tic_tac,KMST.KMST,Quiz.Quiz,SodukoSolver.SodukoSolver]
print('Available games -: \n\n 1. Bollywood\n 2.Tic Tac Toe \n 3. Raja Mantri Chor Sepai \n 4.Matrix \n 5. Soduko Solver')
try:
	choice = int(input('[?] Select game : '))
except Exception:
	print('[!] Select using number only!')
else:
	if choice >len(games):
		quit(0)
user = input('[.] Start Game (y/n) ..').lower()
if user == 'y':
	run = True
	
	games[choice-1]().Start_game()

	
if not run:
	print('// Sad You Dont like em :(  // ')
else:
	print(' Thanks for Playing')