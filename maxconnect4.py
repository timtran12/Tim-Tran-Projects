#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Dr. Vassilis Athitsos
# Written to be Python 2.4 compatible for omega

from itertools import count
import sys
from MaxConnect4Game import *

def oneMoveGame(currentGame, depth):
    if currentGame.pieceCount == 42:    # Is the board full already?
        print ('BOARD FULL\n\nGame Over!\n')
        sys.exit(0)

    currentGame.aiPlay(depth) # Make a move (only random is implemented)

    print ('Game state after move:')
    currentGame.printGameBoard()

    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()


def interactiveGame(currentGame, next_player, depth):    
    while (currentGame.pieceCount != 42):
    
        if(next_player == "computer-next"):
            currentGame.currentTurn = 1
            currentGame.printGameBoard()
            currentGame.countScore()
            currentGame.gameFile = open("computer.txt", 'w')
            
            currentGame.aiPlay(depth)
        
        currentGame.currentTurn = 2
        currentGame.printGameBoard()
        currentGame.countScore()
        
        currentGame.gameFile = open("human.txt", "w") 
        
        column = int(input("Choose a column to play in: "))
        
        valid = currentGame.playPiece(currentGame.gameBoard, column)
        while not(valid):
            print("Move not valid! Choose another column!")
            valid = currentGame.playPiece(currentGame.gameBoard, column, currentGame.currentTurn)
            
        currentGame.pieceCount += 1
        
        currentGame.printGameBoardToFile()
        currentGame.gameFile.close
        
    if currentGame.pieceCount == 42:    # Is the board full already?
        if currentGame.player1Score > currentGame.player2Score:
            print("Player 1 wins")
            
        if currentGame.player1Score == currentGame.player2Score:
            print("Tie")
            
        if currentGame.player1Score < currentGame.player2Score:
            print("Player 2 wins")
            
        print("Game Over")
        print ('BOARD FULL\n\nGame Over!\n')
        sys.exit(0)

def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print ('Four command-line arguments are needed:')
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]
    depth = argv[4]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game() # Create a game

    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gameFile.close()

    print ('\nMaxConnect-4 game\n')
    print ('Game state before move:')
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        next_player = argv[3]
        interactiveGame(currentGame, next_player, int(depth)) # Be sure to pass whatever else you need from the command line
    else: # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame, int(depth)) # Be sure to pass any other arguments from the command line you might need.


if __name__ == '__main__':
    main(sys.argv)



