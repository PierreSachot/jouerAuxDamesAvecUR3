# -*- coding:utf-8 -*-
import cv2
import math
import numpy as np
from Case import Case

imgBase = cv2.imread('Images/grillePions.jpg')
gray_img = cv2.cvtColor(imgBase, cv2.COLOR_BGR2GRAY)
template = cv2.imread('Images/pattern.png')
gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
w, h = gray_template.shape[::-1]
nbCasesParLignes = 10

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

img = imgBase.copy()
method = eval(methods[1])

# Apply template Matching
res = cv2.matchTemplate(img,template,method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

top_right =  (top_left[0] + w, top_left[1])
bottom_left = (top_left[0], top_left[1] + h)

tailleCarreauX = (top_right[0]-top_left[0])/nbCasesParLignes
tailleCarreauY = (bottom_right[1]-top_right[1])/nbCasesParLignes

#creation des points
pointsList = []
for i in range(0, 11):
    pointsList.append([])
    for j in range(0,11):
        pointsList[i].append([])

pointPrecedent = top_right
currentPoint = top_right
for x in range(0,11):
    currentPoint = (top_right[0]-x*tailleCarreauX, top_right[1])
    pointPrecedent = currentPoint
    pointsList[x][0] = currentPoint
    for y in range(1,11):
        currentPoint = (pointPrecedent[0], pointPrecedent[1]+tailleCarreauY)
        pointsList[x][y] = currentPoint
        pointPrecedent = currentPoint

#creation des cases dans une liste
listecases = []
for y in range(0,10):
    listecases.append([])
    for x in range(0,10):
        listecases[y].append([])
        maCase = Case(pointsList[y][x], pointsList[y][x+1],pointsList[y+1][x],pointsList[y+1][x+1])
        listecases[y][x] = maCase
#print(listecases)

currentIndex = (9,9)
cv2.line(imgBase, listecases[currentIndex[0]][currentIndex[1]].top_left, listecases[currentIndex[0]][currentIndex[1]].top_right, (0, 255, 0), 2)
cv2.line(imgBase, listecases[currentIndex[0]][currentIndex[1]].top_right, listecases[currentIndex[0]][currentIndex[1]].bottom_right, (0, 255, 0), 2)
cv2.line(imgBase, listecases[currentIndex[0]][currentIndex[1]].top_left, listecases[currentIndex[0]][currentIndex[1]].bottom_left, (0, 255, 0), 2)
cv2.line(imgBase, listecases[currentIndex[0]][currentIndex[1]].bottom_left, listecases[currentIndex[0]][currentIndex[1]].bottom_right, (0, 255, 0), 2)
        
#cv2.rectangle(img,top_left, bottom_right, 255, 2)



#Détection des pions
for y in range(0,10):
    for x in range(0,10):
        milieuCase = (listecases[y][x].bottom_right[0]+(listecases[y][x].bottom_right[0] - listecases[y][x].top_left[0])/2, listecases[y][x].bottom_right[1]+(listecases[y][x].bottom_right[1] - listecases[y][x].top_left[1])/2)
        cv2.circle(imgBase, milieuCase, 5, (0, 255, 0), -1)

cv2.imshow('Corners', imgBase)

cv2.waitKey(0)  # waits until a key is pressed

cv2.destroyAllWindows()  # destroys the window showing image
 
