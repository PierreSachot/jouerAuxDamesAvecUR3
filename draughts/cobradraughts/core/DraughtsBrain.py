#    This file is part of CobraDraughts.
#
#    CobraDraughts is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    CobraDraughts is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with CobraDraughts.  If not, see <http://www.gnu.org/licenses/>.
'''
Created on Jul 21, 2011

@author: Davide Aversa
@version: 1.1

DraughtsBrain module contains DraughtsBrain class and related stuff.
'''

import random
import time

import sys
import os.path

#linux
sys.path.append('/home/constant/Documents/jouerAuxDamesAvecUR3/')

from draughts.cobradraughts.core.DBoard import DBoard
from ur3Scripts import move
from prehenseurVentouse import prehenseur
from traitementVideo import board

__author__ = "Davide Aversa"
__copyright__ = "Copyright 2011"
__credits__ = ["Davide Aversa", ]
__license__ = "GPLv3"
__version__ = "1.1"
__maintainer__ = "Davide Aversa"
__email__ = "thek3nger@gmail.com"
__status__ = "Production"

# Solve Python 3/2 range performance issue.
try:
    range = xrange  # Use Python 2.x @ReservedAssignment
except:
    pass  # Use Python 3.x


class DraughtsBrain(object):
    '''
    Class AI for Draughts.

    Use Min-Max with Alpha-Beta Prune.
    '''

    def __init__(self, weights, horizon, weights_bis=None, verbose=False):
        '''
        Constructor

        ARGS:
            @param weights: Weights for board Static-Evaluation-Function.
            @param horizon: Max level for the search algorithm.
            @param weights_bis: Weights for the dark-side AI.
        '''
        self.weights = weights
        self.horizon = horizon

        self.move = 0
        self.board = DBoard()
        self.turn = 'LIGHT'

        self.gameover = False
        self.winner = None
        self.nocapturecounter = 0  # Move without a capture.

        self.verbose = verbose

        if weights_bis is None:
            self.weights_bis = self.weights
        else:
            self.weights_bis = weights_bis

    def reset(self):
        '''
        Reset this brain.

        @deprecated: This method can be deleted in future releases.
        '''
        self.move = 0
        self.board = DBoard()
        self.turn = 'LIGHT'
        self.gameover = False
        self.nocapturecounter = 0

    def switch_turn(self):
        '''
        Switch current in-game player.
        '''
        if self.turn == 'LIGHT':
            self.turn = 'DARK'
        else:
            self.turn = 'LIGHT'

    def _switch_player(self, player):
        '''
        Switch player tag.

        ARGS:
            @param player: Current player.

        RETURN:
            @return: Next Player.
        '''
        if player == 'LIGHT':
            return 'DARK'
        else:
            return 'LIGHT'

    def run_self(self):
        '''
        Execute "selfish" AI vs. AI match.
        '''
        
        self.gameover = False
        while not self.gameover and self.nocapturecounter < 50:
            if(self.turn=='LIGHT'):
                self.__init__(self.weights,self.horizon,self.weights_bis,self.verbose)
                raw_input("Tour joueur") #raw input python 2, input python3
                self.board=board.get_board()
                print(self.board)
                self.switch_turn()

            else:
                bestmove = self.best_move()
                if not bestmove:
                    self.winner = self._switch_player(self.turn)  # No valid move!
                    break

                print(self.turn)
                self.pickAndPlace(bestmove)
                self.apply_action(bestmove)

                if self.verbose:
                    print(self.board)
                    #print(self.board.board_score(self.weights))

        if not self.gameover:  # So, too-much noncapture.
            self.winner = 'DRAW'
        return self.winner

    def apply_action(self, action):
        '''
        Apply an action to board.

        ARGS:
            @param action: Action that it's going to be executed.
        '''
        self.board.apply_action(action)

        self.move += 1
        if len(self.board.light_pieces) == 0:
            self.gameover = True
            self.winner = 'DARK'
        elif len(self.board.dark_pieces) == 0:
            self.gameover = True
            self.winner = 'LIGHT'
        else:
            if action.type=='CAPTURE':
                self.pickAndDestroy(action)
            self.switch_turn()
            if action.type != 'CAPTURE':
                self.nocapturecounter += 1
            else:
                self.nocapturecounter = 0

    def pickAndPlace(self,action):
        # Get Source and Destination.
        srow, scol = action.source
        drow, dcol = action.destination
        move.PlayPose()
        move.Cords(0, 0, srow, scol)
        move.Down(0.0175)
        prehenseur.Aspire()
        time.sleep(1.5)
        move.Up(0.0175)
        time.sleep(0.5)
        move.Cords(srow, scol, drow, dcol)
        move.Down(0.0175)
        prehenseur.Stop()
        time.sleep(1.5)
        move.Up(0.0175)
        time.sleep(0.5)
        if(action.capture!='CAPTURE'):
            move.WaitPose()

    def pickAndDestroy(self,action):
        # Get Source and Destination.
        z=0.014
        srow, scol = action.source
        drow, dcol = action.destination
        testRow = (drow + srow)/2
        testCol = (scol + dcol)/2
        action.destination = testRow, testCol
        action.source = action.destination
        move.PlayPose()
        move.Cords(0, 0, testRow, testCol)
        move.Down(z)
        prehenseur.Aspire()
        time.sleep(1.5)
        move.Up(z)
        time.sleep(0.5)
        move.Cords(testRow,testCol, -1, 5)
        move.Down(z)
        prehenseur.Stop()
        time.sleep(1.5)
        move.Up(z)
        time.sleep(0.5)
        move.WaitPose()
# (5,4) et (3,6) => (4,5)
    ########
    ## AI ##
    ########

    def best_move(self):
        '''
        Find the next best move according current player state.

        This method use the Min-Max algorithm wit Alpha-Beta pruning system
        to minimize the number of explored nodes.

        RETURN:
            @return: One of the best move.
        '''
        if len(self.board.all_move(self.turn)) == 0:
            self.gameover = True
            self.winner = self._switch_player(self.turn)
            return None

        self.path = []
        if self.turn == 'LIGHT':
            value = self.alphabeta(-float('inf'), float('inf'), self.horizon, self.turn, self.weights)
        else:
            value = self.alphabeta(-float('inf'), float('inf'), self.horizon, self.turn, self.weights_bis)

        bestmoves = []

        for element in self.path:
            if element[1] == value:  # Find path with value equal to best-value.
                bestmoves.append(element[0])
        else:
            if len(bestmoves) == 0 and len(self.path) != 0:  # If path is not empty return first value.
                print("Woops!")
                return self.path[0][0]  # WARNING: This code should never be executed.

        selected_move = random.choice(bestmoves)  # Select randomly a move among the best ones.
        return selected_move

    def alphabeta(self, alpha, beta, level, player, weights):
        '''
        THE GLORIOUS ALPHA-BETA ALGORITHM. GLORIFY HIM.

        ARGS:
            @param aplha: Current Alpha Value.
            @param beta: Current Beta Value.
            @param level: Current Level.
            @param player: Current Player.
            @param weights: Set of weights to use. TODO: Can remove this?

        RETURN
        '''
        if level == 0:
            value = self.board.board_score(weights)
            self.path.append((self.board.movelist[self.move], value))
            return value
        if player == 'LIGHT':
            moves = self.board.all_move(player)
            v = -float('inf')
            for mov in moves:
                self.board.apply_action(mov)
                v = max(v, self.alphabeta(alpha, beta, level - 1, self._switch_player(player), weights))
                self.board.undo_last()
                if beta <= v:
                    return v
                alpha = max(alpha, v)
            if len(moves) == 0:
                self.path.append((self.board.movelist[self.move], v))
            return v
        else:
            moves = self.board.all_move(player)
            v = float('inf')
            for mov in moves:

                self.board.apply_action(mov)
                v = min(v, self.alphabeta(alpha, beta, level - 1, self._switch_player(player), weights))
                self.board.undo_last()
                if v <= alpha:
                    return v
                beta = min(beta, v)
            if len(moves) == 0:
                self.path.append((self.board.movelist[self.move], v))
            return v

