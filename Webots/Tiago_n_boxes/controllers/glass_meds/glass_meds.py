from controller import Robot, Motor, Keyboard

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = 64

leftArm1 = robot.getDevice('arm_left_1_joint')
rightArm1 = robot.getDevice('arm_right_1_joint')
leftArm1.setPosition(0.7)
rightArm1.setPosition(0.7)

#leftArm2 = robot.getDevice('arm_left_2_joint')
#rightArm2 = robot.getDevice('arm_right_2_joint')
#leftArm2.setPosition(1.5)
#rightArm2.setPosition(1.5)

leftArm3 = robot.getDevice('arm_left_3_joint')
rightArm3 = robot.getDevice('arm_right_3_joint')
leftArm3.setPosition(1.6)
rightArm3.setPosition(1)

leftArm4 = robot.getDevice('arm_left_4_joint')
rightArm4 = robot.getDevice('arm_right_4_joint')
leftArm4.setPosition(1.5)
rightArm4.setPosition(0.5)

leftGripl = robot.getDevice('left_hand_gripper_left_finger_joint')
rightGripl = robot.getDevice('right_hand_gripper_left_finger_joint')
leftGripl.setPosition(0.02)
rightGripl.setPosition(0.044)

leftGripr = robot.getDevice('left_hand_gripper_right_finger_joint')
rightGripr = robot.getDevice('right_hand_gripper_right_finger_joint')
leftGripr.setPosition(0.03)
rightGripr.setPosition(0.044)


leftMotor = robot.getDevice('wheel_left_joint')
rightMotor = robot.getDevice('wheel_right_joint')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)


#key=Keyboard.getKey()
initime=robot.getTime()

while robot.step(timestep) != -1:
    time = robot.getTime() - initime
    if (time<2):
      l_vel=-0.5
      r_vel=-0.5
    elif (time<40):
      l_vel=10.0
      r_vel=-10.0
    elif (time<72):
      l_vel=0.5
      r_vel=0.5
    elif (time<76):
      l_vel=0.0
      r_vel=0.0
      leftGripl.setPosition(0.04)
      leftGripr.setPosition(0.04)
    else:
      l_vel=-0.5
      r_vel=-0.5
    print('time',time)
    print('lvel,rvel',l_vel,r_vel)
    leftMotor.setVelocity(l_vel)
    rightMotor.setVelocity(r_vel)
    