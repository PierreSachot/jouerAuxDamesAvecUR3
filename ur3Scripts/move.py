import urx

'''

PLACER FEUILLE A 11.5 CM DE LA BASE DU ROBOT

'''

def WaitPose():
    rob = urx.Robot("10.55.55.41")
    rob.set_tcp((0, 0, 0, 0, 0, 0))
    waitPose = [4.7123332023620605, -1.5709040800677698, -1.570632282887594, 6.103515625e-05, 1.5707645416259766,
                 -2.366701234990387e-05]
    rob.movej(waitPose, acc=1, vel=0.5)


def PlayPose():
    rob = urx.Robot("10.55.55.41")
    rob.set_tcp((0, 0, 0, 0, 0, 0))
    playPose = [4.639049530029297, -2.924447838460104, -0.6361406485186976, -1.1187346617328089, 1.5790801048278809,
                -0.047751728688375294]  # coord[0,0]
    rob.movej(playPose, acc=1, vel=0.5)


def Cords(previousX,previousY,x,y):
    rob = urx.Robot("10.55.55.41")
    rob.set_tcp((0, 0, 0, 0, 0, 0))

    if(previousX!=0):

        x=-1*(previousX-x)


    if(previousY!=0):
        y=-1*(previousY-y)

    rob.translate((0.028 * x, 0.028 * y, 0), 1, 0.5)  # 0.028 = 2.8cm

def Up():
    rob = urx.Robot("10.55.55.41")
    rob.set_tcp((0, 0, 0, 0, 0, 0))
    rob.translate((0, 0, 0.014), 0.5, 0.25)

def Down():
    rob = urx.Robot("10.55.55.41")
    rob.set_tcp((0, 0, 0, 0, 0, 0))
    rob.translate((0, 0, -0.014), 0.5, 0.25)




