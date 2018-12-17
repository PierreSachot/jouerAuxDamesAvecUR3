# -*- coding:utf-8 -*-

from BoardDetector import BoardDetector
import cv2

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    bd = BoardDetector(frame,
                       cv2.imread(
                           '/run/media/pierre/Partage/Documents/ENSC/2ème année/S7/Transpromo/Projet UR3/jouerAuxDamesAvecUR3/traitementVideo/Images/pattern.png'),
                       10)
    # On trouve le damier dans l'image
    bd.findTemplate()
    # On créer l'objet board.
    board, imgBase = bd.createBoard(11, 11)
    cv2.imshow('frame', imgBase)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
