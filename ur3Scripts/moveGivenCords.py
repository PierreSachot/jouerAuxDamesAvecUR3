import urx
import time

'''

PLACER FEUILLE A 11.5 CM DE LA BASE DU ROBOT

'''

rob = urx.Robot("10.55.55.41")
rob.set_tcp((0, 0, 0, 0, 0, 0))
startPose=[4.7123332023620605, -1.5709040800677698, -1.570632282887594, 6.103515625e-05, 1.5707645416259766, -2.366701234990387e-05]
#playPose=[5.6446852684021, -2.210615936909811, -2.59827167192568, 0.10437619686126709, 1.564775824546814, 0.9693077206611633] #coord [0,0]
playPose=[4.639049530029297, -2.924447838460104, -0.6361406485186976, -1.1187346617328089, 1.5790801048278809, -0.047751728688375294]#coord[9,9]
print ("Deplacement position attente")
rob.movej(startPose, acc=1, vel=0.5)
time.sleep(1)
print ("Deplacement position jeu")
rob.movej(playPose, acc=1, vel=0.5)


previousX=0;
previousY=0;
#hypothenus=sqrt(2cote)
while True:
    print("entrer x (-1 pour arreter)")
    x = input()
    if(x==-1):
        break
    print("entrer y")
    y= input()
    if(previousX!=0):
        temp=x
        x=-1*(previousX-x)
        previousX=temp
    else:
        previousX=x

    if(previousY!=0):
        temp=y
        y=-1*(previousY-y)
        previousY=temp
    else:
        previousY=y


    print("x:",x)
    print("y:",y)
    rob.translate((0.028 * x, 0.028 * y, 0), 1, 0.5)  # 0.028 = 2.8cm



time.sleep(1)
print("Deplacement position attente")
rob.movej(startPose,acc=1,vel=0.5)


