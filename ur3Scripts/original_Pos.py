import urx

rob = urx.Robot("10.55.55.41")
rob.set_tcp((0, 0, 0, 0, 0, 0))
joint_pose=rob.getj()
print "start joint pose: ",  joint_pose
