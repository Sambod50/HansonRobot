from morse.builder import *
robot =Morsy()

motion = MotionVW()
motion.translate(z=0.43)
robot.append(motion)

pose = Pose()
pose.translate(z=0.74)
robot.append(pose)
pose.add_stream('ros')
motion.add_stream('ros')
env = Environment('indoors-1/indoor-1')
env.set_camera_location([5,-5,6])
env.set_camera_rotation([1.047,0,0.7854])

