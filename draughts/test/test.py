'''
Created on Jul 22, 2011

@author: Davide Aversa
'''

import sys
import os.path

#linux
sys.path.append('/home/constant/Documents/jouerAuxDamesAvecUR3/')

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#from cobradraughts.core.DraughtsBrain import DraughtsBrain
from draughts.cobradraughts.core.DraughtsBrain import DraughtsBrain

weights1 = {'PIECE':400,
          'KING':1200,
          'BACK':10,
          'KBACK':10,
          'CENTER':30,
          'KCENTER':30,
          'FRONT':60,
          'KFRONT':60,
          'MOB':0}

weights2 = {'PIECE':400,
          'KING':800,
          'BACK':40,
          'KBACK':40,
          'CENTER':40,
          'KCENTER':40,
          'FRONT':60,
          'KFRONT':60,
          'MOB':0}

# Exemple
D = DraughtsBrain(weights1, 2, weights2,verbose=True)
D.run_self()

for p in D.board.dark_pieces:
    print(p.position)



print("The winner is %s!" % D.winner)
time = input("Mettre fin au programme: ")