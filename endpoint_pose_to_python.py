#!/usr/bin/python
import baxter_interface
import rospy

rospy.init_node("test2")
left = baxter_interface.Limb('left')
pose =  left.endpoint_pose()
print "pos = Point(x=" + str(pose['position'].x)+ ","
print "y=" + str(pose['position'].y) + ","
print "z=" + str(pose['position'].z) + ")"
print "quat = Quaternion(x=" + str(pose['orientation'].x) + ","
print "y="+ str(pose['orientation'].y) + ","
print "z="+str(pose['orientation'].z) + ","
print "w="+str(pose['orientation'].w) + ")"
print left.joint_angles()
