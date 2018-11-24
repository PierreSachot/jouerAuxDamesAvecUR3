import urx
import time
import sys

rob = urx.Robot("10.55.55.41")
rob.set_tcp((0, 0, 0, 0, 0, 0))
startPose=[4.7123332023620605, -1.5709040800677698, -1.570632282887594, 6.103515625e-05, 1.5707645416259766, -2.366701234990387e-05]
playPose=[4.712381362915039, -2.264529530202047, -2.0901554266559046, -0.28888065019716436, 1.5723270177841187, 0.0]
print "Deplacement position attente"
rob.movej(startPose,acc=1,vel=0.5)
time.sleep(1)
print "Deplacement position jeu"
#hypothenus=sqrt(2cote)
dg=7.07106781187
dg=dg*0.01;
rob.movej(playPose,acc=1,vel=0.5)
x=1
while(x!=0):
	print "1= gauche, 2=droite,3=haut,4=bas,5=diagonal-gauche-arriere,6=diagonal-droite-avant(oppose de 5),7=diagonale-droite-arriere,8=diagonale-gauche-avant"
	x = input()
	if x==1:
		rob.translate((0.05, 0, 0), 1, 0.5)
		time.sleep(1)
	elif x==2:
		rob.translate((-0.05, 0, 0), 1, 0.5)
		time.sleep(1)
	elif x==3:
		rob.translate((0, 0, 0.05), 1, 0.5)
		time.sleep(1)
	elif x==4:
		rob.translate((0,0,-0.05),1,0.5)
		time.sleep(1)
	elif x==5:
		rob.translate((0.05,0.05,0),1,0.5)
		time.sleep(1)
	elif x==6:
		rob.translate((-0.05,-0.05,0),1,0.5)
		time.sleep(1)
	elif x==7:
		rob.translate((-0.05,0.05,0),1,0.5)
		time.sleep(1)
	elif x==8:
		rob.translate((0.05,-0.05,0),1,0.5)
		time.sleep(1)
	elif x==0:
		print rob.getj()
		break


time.sleep(1)
print "Deplacement position attente"
rob.movej(startPose,acc=1,vel=0.5)
sys.exit()
'''
joint_pose=rob.getj()
print "start joint pose: ",  rob.getj()	
print "move 0.1 on x axis (gauche)"
rob.translate((0.1, 0, 0), 1, 0.5)
time.sleep(1)
print "move 0.1 on y axis (recule)"
rob.translate((0, 0.1, 0), 1, 0.5)  
time.sleep(1)
print "move 0.1 on z axis(monte)"
rob.translate((0, 0, 0.1), 1, 0.5)  
time.sleep(1)
print "go back to original pos"
rob.movej(joint_pose, acc=1, vel=0.5)
'''
