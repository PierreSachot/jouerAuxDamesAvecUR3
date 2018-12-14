# -*- coding:utf-8 -*-
import cv2
from BoardDetector import BoardDetector


cap = cv2.VideoCapture(2)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # On créer le detecteur du damier
    bd = BoardDetector(frame, cv2.imread('Images/pattern.png'), 10)
    # On trouve le damier dans l'image
    bd.findTemplate()
    # On créer l'objet board.
    board, imgBase = bd.createBoard(11,11)

    # Display the resulting frame
    cv2.imshow('frame',imgBase)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

#from traitementVideo.board import get_board


#while(True):
#    print(get_board())
