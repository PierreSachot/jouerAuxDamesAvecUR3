# -*- coding:utf-8 -*-
import cv2

from traitementVideo.Case import Case
from draughts.cobradraughts.core.DBoard import DBoard
from draughts.cobradraughts.core.DPiece import DPiece

class BoardDetector:
    def __init__(self, imageToAnalyze, pattern, nbSquarePerLines):
        self.originalImg = imageToAnalyze
        self.pattern = pattern
        self.grayImg = cv2.cvtColor(self.originalImg, cv2.COLOR_BGR2GRAY)
        self.grayPattern = cv2.cvtColor(self.pattern, cv2.COLOR_BGR2GRAY)
        self.w, self.h = self.grayPattern.shape[::-1]
        self.nbSquarePerLines = nbSquarePerLines
        self.top_left = ()
        self.top_right = ()
        self.bottom_left = ()
        self.bottom_right = ()
        self.squareSizeX = 0
        self.squareSizeY = 0

    def findTemplate(self):
        # All the 6 methods for comparison in a list
        methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                   'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

        img = self.originalImg.copy()
        method = eval(methods[1])
        # Apply template Matching
        res = cv2.matchTemplate(img, self.pattern, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            self.top_left = min_loc
        else:
            self.top_left = max_loc
        self.bottom_right = (self.top_left[0] + self.w, self.top_left[1] + self.h)

        self.top_right = (self.top_left[0] + self.w, self.top_left[1])
        self.bottom_left = (self.top_left[0], self.top_left[1] + self.h)
        self.squareSizeX = (self.top_right[0] - self.top_left[0]) / self.nbSquarePerLines
        self.squareSizeY = (self.bottom_right[1] - self.top_right[1]) / self.nbSquarePerLines

    def createBoard(self):
        # creation des points
        pointsList = []
        for i in range(0, 11):
            pointsList.append([])
            for j in range(0, 11):
                pointsList[i].append([])

        pointPrecedent = self.top_right
        currentPoint = self.top_right
        for x in range(0, 11):
            currentPoint = (self.top_right[0] - x * self.nbSquarePerLines - 1, self.top_right[1])
            pointPrecedent = currentPoint
            pointsList[x][0] = currentPoint
            for y in range(1, 11):
                currentPoint = (pointPrecedent[0], pointPrecedent[1] + self.nbSquarePerLines + 1)
                pointsList[x][y] = currentPoint
                pointPrecedent = currentPoint

        # creation des cases dans une liste
        listecases = []
        for y in range(0, 10):
            listecases.append([])
            for x in range(0, 10):
                listecases[y].append([])
                maCase = Case(pointsList[y][x], pointsList[y][x + 1], pointsList[y + 1][x], pointsList[y + 1][x + 1])
                listecases[y][x] = maCase

        board = DBoard()
        board.light_pieces = []
        board.dark_pieces = []
        board.bitmap = [None] * 50
        # Détection des pions
        for y in range(0, 10):
            for x in range(0, 10):
                milieuCase = (
                    listecases[y][x].top_left[0] + (
                                listecases[y][x].bottom_right[0] - listecases[y][x].top_left[0]) / 2,
                    listecases[y][x].top_left[1] + (
                                listecases[y][x].bottom_right[1] - listecases[y][x].top_left[1]) / 2)
                b = self.originalImg[milieuCase[1], milieuCase[0], 0]
                g = self.originalImg[milieuCase[1], milieuCase[0], 1]
                r = self.originalImg[milieuCase[1], milieuCase[0], 2]
                if b < 100 and g > 87:
                    new_piece = DPiece(board, y, x, 'LIGHT')
                    board.light_pieces.append(new_piece)
                    board.set_bitmap(y, x, new_piece)
                    cv2.circle(self.originalImg, milieuCase, 2, (255, 0, 0),
                               -1)  # Pions vert wallah ! ==> pions LIGHT sur damier
                else:
                    if r < 100 and b > 100:
                        new_piece = DPiece(board, y, x, 'DARK')
                        board.dark_pieces.append(new_piece)
                        board.set_bitmap(y, x, new_piece)
                        cv2.circle(self.originalImg, milieuCase, 2, (0, 0, 255),
                                   -1)  # Pions bleus wallah ! ==> pions DARK sur damier
        return board, self.originalImg