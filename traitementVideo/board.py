# -*- coding:utf-8 -*-
import cv2
from BoardDetector import BoardDetector

def get_board():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    # On créer le detecteur du damier
    bd = BoardDetector(frame, cv2.imread('/home/constant/Documents/jouerAuxDamesAvecUR3/traitementVideo/Images/pattern.png'), 10)
    # On trouve le damier dans l'image
    bd.findTemplate()
    # On créer l'objet board.
    board, imgBase = bd.createBoard(11, 11)
    cap.release()
    return board

