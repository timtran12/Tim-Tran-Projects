#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Vassilis Athitsos
# Written to be Python 2.4 compatible for omega

from copy import deepcopy
import random, math
import sys

class maxConnect4Game:
    def __init__(self):
        self.gameBoard = [[0 for i in range(7)] for j in range(6)]
        self.currentTurn = 1
        self.player1Score = 0
        self.player2Score = 0
        self.pieceCount = 0
        self.gameFile = None
        random.seed()

    # Count the number of pieces already played
    def checkPieceCount(self):
        self.pieceCount = sum(1 for row in self.gameBoard for piece in row if piece)

    # Output current game status to console
    def printGameBoard(self):
        print (' -----------------')
        
        for i in range(6):
            print (' |',end='')
            for j in range(7):
                print('%d' % self.gameBoard[i][j], end=''),
            print ('| ',)
            
        print (' -----------------')

    # Output current game status to file
    def printGameBoardToFile(self):
        for row in self.gameBoard:
            self.gameFile.write(''.join(str(col) for col in row) + '\r')
            
        self.gameFile.write('%s\r' % str(self.currentTurn))

    # Place the current player's piece in the requested column
    def playPiece(self, gameBoard, column):
        if not gameBoard[0][column]:
            for i in range(5, -1, -1):
                if not gameBoard[i][column]:
                    gameBoard[i][column] = self.currentTurn
                    return 1
                
    def minimax(self, gameBoard, depth, max_player, alpha, beta):
        if(depth == 0):
            value = self.num_consecutive(gameBoard)
            return value, 0
        if(max_player):
            bestValue = -math.inf
            for i in range(7):
                gameBoard_new = deepcopy(gameBoard)
                if(self.playPiece(gameBoard_new, i)):
                    value, max_col = self.minimax(gameBoard_new, depth-1, False, alpha, beta)
                    if(bestValue < value):
                        col = i
                        bestValue = value
                    alpha = max(alpha, bestValue)
                    if(beta <= alpha):
                        break
                else:
                    continue
            return bestValue, col
        
        else:
            bestValue = math.inf
            for i in range(7):
                gameBoard_new = deepcopy(gameBoard)
                self.playPiece(gameBoard_new, i)
                value, col = self.minimax(gameBoard_new, depth-1, True, alpha, beta)
                if(bestValue > value):
                    col = i
                    bestValue = value
                alpha = min(alpha, bestValue)
                if(beta <= alpha):
                    break
            return bestValue, col
        
    def find_score(self, board):
        value = 0
        value = value+self.count_vert(board)
                
        value = value+self.count_hor(board)
                
        value = value+self.count_diag(board)
    
        return value

    def count_vert(self, board):
        counts = 0
    
        for i in range(3):
            for j in range(6):
                if(board[i][j] == self.currentTurn and board[i+1][j] == self.currentTurn and board[i+2][j] == self.currentTurn and board[i+3][j] == self.currentTurn):
                    counts+=100
                elif(board[i][j] == self.currentTurn and board[i+1][j] == self.currentTurn and board[i+2][j] == self.currentTurn):
                    counts+=5
                elif(board[i][j] == self.currentTurn and board[i+1][j] == self.currentTurn):
                    counts+=1
                if(board[i][j] == 1 and board[i+1][j] == 1 and board[i+2][j] == 1 and board[i+3][j] == 1):
                    counts-=5
    
        return counts

    def count_hor(self, board):
        counts = 0
    
        for i in range(6):
            for j in range(4):
                if(board[i][j] == self.currentTurn and board[i][j+1] == self.currentTurn and board[i][j+2] == self.currentTurn and board[i][j+3] == self.currentTurn):
                    counts+=100
                elif(board[i][j] == self.currentTurn and board[i][j+1] == self.currentTurn and board[i][j+2] == self.currentTurn):
                    counts+=5
                elif(board[i][j] == self.currentTurn and board[i][j+1] == self.currentTurn):
                    counts+=1
                if(board[i][j] == 1 and board[i][j+1] == 1 and board[i][j+2] == 1 and board[i][j+3] == 1):
                    counts-=5
    
        return counts

    def count_diag(self, board):
        counts = 0
        for i in range(3):
            for j in range(4):
                if(board[i][j] == self.currentTurn and board[i+1][j+1] == self.currentTurn and board[i+2][j+2] == self.currentTurn and board[i+3][j+3] == self.currentTurn):
                    counts+=100
                elif(board[i][j] == self.currentTurn and board[i+1][j+1] == self.currentTurn and board[i+2][j+2] == self.currentTurn):
                    counts+=5
                elif(board[i][j] == self.currentTurn and board[i+1][j+1] == self.currentTurn):
                    counts+=1
                if(board[i][j] == 1 and board[i+1][j+1] == 1 and board[i+2][j+2] == 1 and board[i+3][j+3] == 1):
                    counts-=5
        
        for i in range(3):
            for j in range(4):
                if(board[i+3][j] == self.currentTurn and board[i+2][j+1] == self.currentTurn and board[i+1][j+2] == self.currentTurn and board[i][j+3] == self.currentTurn):
                    counts+=100
                elif(board[i+3][j] == self.currentTurn and board[i+2][j+1] == self.currentTurn and board[i+1][j+2] == self.currentTurn):
                    counts+=5
                elif(board[i+3][j] == self.currentTurn and board[i+2][j+1] == self.currentTurn):
                    counts+=1
                if(board[i+3][j] == 1 and board[i+2][j+1] == 1 and board[i+1][j+2] == 1 and board[i][j+3] == 1):
                    counts-=5
        return counts

    def num_consecutive(self, gameBoard):
        score = 0
        center_array = []
        for i in range(6):
            center_array.append(gameBoard[i][3])
            if(gameBoard[i][3] == self.currentTurn):
                yes = 0
        center_score = center_array.count(self.currentTurn)
        score+=center_score*3
        score += self.find_score(gameBoard)
        return score

    # The AI section. Currently plays randomly.
    def aiPlay(self, depth):
        score, randColumn = self.minimax(self.gameBoard, depth, True, -math.inf, math.inf)
        result = self.playPiece(self.gameBoard, randColumn)
        self.pieceCount += 1
        if not result:
            self.aiPlay(depth)
        else:
            print('\n\nmove %d: Player %d, column %d\n' % (self.pieceCount, self.currentTurn, randColumn+1))
            if self.currentTurn == 1:
                self.currentTurn = 2
            elif self.currentTurn == 2:
                self.currentTurn = 1

    # Calculate the number of 4-in-a-row each player has
    def countScore(self):
        self.player1Score = 0
        self.player2Score = 0

        # Check horizontally
        for row in self.gameBoard:
            # Check player 1
            if row[0:4] == [1]*4:
                self.player1Score += 1
            if row[1:5] == [1]*4:
                self.player1Score += 1
            if row[2:6] == [1]*4:
                self.player1Score += 1
            if row[3:7] == [1]*4:
                self.player1Score += 1
            # Check player 2
            if row[0:4] == [2]*4:
                self.player2Score += 1
            if row[1:5] == [2]*4:
                self.player2Score += 1
            if row[2:6] == [2]*4:
                self.player2Score += 1
            if row[3:7] == [2]*4:
                self.player2Score += 1

        # Check vertically
        for j in range(7):
            # Check player 1
            if (self.gameBoard[0][j] == 1 and self.gameBoard[1][j] == 1 and
                   self.gameBoard[2][j] == 1 and self.gameBoard[3][j] == 1):
                self.player1Score += 1
            if (self.gameBoard[1][j] == 1 and self.gameBoard[2][j] == 1 and
                   self.gameBoard[3][j] == 1 and self.gameBoard[4][j] == 1):
                self.player1Score += 1
            if (self.gameBoard[2][j] == 1 and self.gameBoard[3][j] == 1 and
                   self.gameBoard[4][j] == 1 and self.gameBoard[5][j] == 1):
                self.player1Score += 1
            # Check player 2
            if (self.gameBoard[0][j] == 2 and self.gameBoard[1][j] == 2 and
                   self.gameBoard[2][j] == 2 and self.gameBoard[3][j] == 2):
                self.player2Score += 1
            if (self.gameBoard[1][j] == 2 and self.gameBoard[2][j] == 2 and
                   self.gameBoard[3][j] == 2 and self.gameBoard[4][j] == 2):
                self.player2Score += 1
            if (self.gameBoard[2][j] == 2 and self.gameBoard[3][j] == 2 and
                   self.gameBoard[4][j] == 2 and self.gameBoard[5][j] == 2):
                self.player2Score += 1

        # Check diagonally

        # Check player 1
        if (self.gameBoard[2][0] == 1 and self.gameBoard[3][1] == 1 and
               self.gameBoard[4][2] == 1 and self.gameBoard[5][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][0] == 1 and self.gameBoard[2][1] == 1 and
               self.gameBoard[3][2] == 1 and self.gameBoard[4][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][1] == 1 and self.gameBoard[3][2] == 1 and
               self.gameBoard[4][3] == 1 and self.gameBoard[5][4] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][0] == 1 and self.gameBoard[1][1] == 1 and
               self.gameBoard[2][2] == 1 and self.gameBoard[3][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][1] == 1 and self.gameBoard[2][2] == 1 and
               self.gameBoard[3][3] == 1 and self.gameBoard[4][4] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][2] == 1 and self.gameBoard[3][3] == 1 and
               self.gameBoard[4][4] == 1 and self.gameBoard[5][5] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][1] == 1 and self.gameBoard[1][2] == 1 and
               self.gameBoard[2][3] == 1 and self.gameBoard[3][4] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][2] == 1 and self.gameBoard[2][3] == 1 and
               self.gameBoard[3][4] == 1 and self.gameBoard[4][5] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][3] == 1 and self.gameBoard[3][4] == 1 and
               self.gameBoard[4][5] == 1 and self.gameBoard[5][6] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][2] == 1 and self.gameBoard[1][3] == 1 and
               self.gameBoard[2][4] == 1 and self.gameBoard[3][5] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][3] == 1 and self.gameBoard[2][4] == 1 and
               self.gameBoard[3][5] == 1 and self.gameBoard[4][6] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][3] == 1 and self.gameBoard[1][4] == 1 and
               self.gameBoard[2][5] == 1 and self.gameBoard[3][6] == 1):
            self.player1Score += 1

        if (self.gameBoard[0][3] == 1 and self.gameBoard[1][2] == 1 and
               self.gameBoard[2][1] == 1 and self.gameBoard[3][0] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][4] == 1 and self.gameBoard[1][3] == 1 and
               self.gameBoard[2][2] == 1 and self.gameBoard[3][1] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][3] == 1 and self.gameBoard[2][2] == 1 and
               self.gameBoard[3][1] == 1 and self.gameBoard[4][0] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][5] == 1 and self.gameBoard[1][4] == 1 and
               self.gameBoard[2][3] == 1 and self.gameBoard[3][2] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][4] == 1 and self.gameBoard[2][3] == 1 and
               self.gameBoard[3][2] == 1 and self.gameBoard[4][1] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][3] == 1 and self.gameBoard[3][2] == 1 and
               self.gameBoard[4][1] == 1 and self.gameBoard[5][0] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][6] == 1 and self.gameBoard[1][5] == 1 and
               self.gameBoard[2][4] == 1 and self.gameBoard[3][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][5] == 1 and self.gameBoard[2][4] == 1 and
               self.gameBoard[3][3] == 1 and self.gameBoard[4][2] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][4] == 1 and self.gameBoard[3][3] == 1 and
               self.gameBoard[4][2] == 1 and self.gameBoard[5][1] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][6] == 1 and self.gameBoard[2][5] == 1 and
               self.gameBoard[3][4] == 1 and self.gameBoard[4][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][5] == 1 and self.gameBoard[3][4] == 1 and
               self.gameBoard[4][3] == 1 and self.gameBoard[5][2] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][6] == 1 and self.gameBoard[3][5] == 1 and
               self.gameBoard[4][4] == 1 and self.gameBoard[5][3] == 1):
            self.player1Score += 1

        # Check player 2
        if (self.gameBoard[2][0] == 2 and self.gameBoard[3][1] == 2 and
               self.gameBoard[4][2] == 2 and self.gameBoard[5][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][0] == 2 and self.gameBoard[2][1] == 2 and
               self.gameBoard[3][2] == 2 and self.gameBoard[4][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][1] == 2 and self.gameBoard[3][2] == 2 and
               self.gameBoard[4][3] == 2 and self.gameBoard[5][4] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][0] == 2 and self.gameBoard[1][1] == 2 and
               self.gameBoard[2][2] == 2 and self.gameBoard[3][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][1] == 2 and self.gameBoard[2][2] == 2 and
               self.gameBoard[3][3] == 2 and self.gameBoard[4][4] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][2] == 2 and self.gameBoard[3][3] == 2 and
               self.gameBoard[4][4] == 2 and self.gameBoard[5][5] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][1] == 2 and self.gameBoard[1][2] == 2 and
               self.gameBoard[2][3] == 2 and self.gameBoard[3][4] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][2] == 2 and self.gameBoard[2][3] == 2 and
               self.gameBoard[3][4] == 2 and self.gameBoard[4][5] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][3] == 2 and self.gameBoard[3][4] == 2 and
               self.gameBoard[4][5] == 2 and self.gameBoard[5][6] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][2] == 2 and self.gameBoard[1][3] == 2 and
               self.gameBoard[2][4] == 2 and self.gameBoard[3][5] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][3] == 2 and self.gameBoard[2][4] == 2 and
               self.gameBoard[3][5] == 2 and self.gameBoard[4][6] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][3] == 2 and self.gameBoard[1][4] == 2 and
               self.gameBoard[2][5] == 2 and self.gameBoard[3][6] == 2):
            self.player2Score += 1

        if (self.gameBoard[0][3] == 2 and self.gameBoard[1][2] == 2 and
               self.gameBoard[2][1] == 2 and self.gameBoard[3][0] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][4] == 2 and self.gameBoard[1][3] == 2 and
               self.gameBoard[2][2] == 2 and self.gameBoard[3][1] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][3] == 2 and self.gameBoard[2][2] == 2 and
               self.gameBoard[3][1] == 2 and self.gameBoard[4][0] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][5] == 2 and self.gameBoard[1][4] == 2 and
               self.gameBoard[2][3] == 2 and self.gameBoard[3][2] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][4] == 2 and self.gameBoard[2][3] == 2 and
               self.gameBoard[3][2] == 2 and self.gameBoard[4][1] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][3] == 2 and self.gameBoard[3][2] == 2 and
               self.gameBoard[4][1] == 2 and self.gameBoard[5][0] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][6] == 2 and self.gameBoard[1][5] == 2 and
               self.gameBoard[2][4] == 2 and self.gameBoard[3][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][5] == 2 and self.gameBoard[2][4] == 2 and
               self.gameBoard[3][3] == 2 and self.gameBoard[4][2] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][4] == 2 and self.gameBoard[3][3] == 2 and
               self.gameBoard[4][2] == 2 and self.gameBoard[5][1] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][6] == 2 and self.gameBoard[2][5] == 2 and
               self.gameBoard[3][4] == 2 and self.gameBoard[4][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][5] == 2 and self.gameBoard[3][4] == 2 and
               self.gameBoard[4][3] == 2 and self.gameBoard[5][2] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][6] == 2 and self.gameBoard[3][5] == 2 and
               self.gameBoard[4][4] == 2 and self.gameBoard[5][3] == 2):
            self.player2Score += 1