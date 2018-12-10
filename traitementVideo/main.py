# -*- coding:utf-8 -*-
import cv2
from BoardDetector import BoardDetector

# On créer le detecteur du damier
bd = BoardDetector(cv2.imread('Images/test.jpg'), cv2.imread('Images/pattern.png'), 10)
# On trouve le damier dans l'image
bd.findTemplate()
# On créer l'objet board.
board, imgBase = bd.createBoard(11,11)

print(board)

cv2.imshow('Corners', imgBase)

cv2.waitKey(0)  # waits until a key is pressed

cv2.destroyAllWindows()  # destroys the window showing image

