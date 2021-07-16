from controller import Robot, Motor, DistanceSensor, Lidar
import math

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = 64

MAX_SPEED = 6.28
CRUISING_SPEED = 5.0
THRESHOLD = 0.01
DECREASE_FACTOR = 10
BACK_SLOWDOWN = 0.9

def gaussian(x, mu, sigma):
  return (1.0 / (sigma * math.sqrt(6.28))) * math.exp(-((x - mu) * (x - mu)) / (2 * sigma * sigma))

lidar = robot.getDevice('Hokuyo URG-04LX-UG01')
lidar.enable(timestep)

width = lidar.getHorizontalResolution()
half_width=width/2
max_range = lidar.getMaxRange()
range_threshold = max_range / 20.0

leftArm1 = robot.getDevice('arm_left_1_joint')
rightArm1 = robot.getDevice('arm_right_1_joint')
leftArm1.setPosition(1.5)
rightArm1.setPosition(1.5)

leftArm2 = robot.getDevice('arm_left_2_joint')
rightArm2 = robot.getDevice('arm_right_2_joint')
leftArm2.setPosition(1.5)
rightArm2.setPosition(1.5)

leftArm3 = robot.getDevice('arm_left_3_joint')
rightArm3 = robot.getDevice('arm_right_3_joint')
leftArm3.setPosition(0.5)
rightArm3.setPosition(0.5)

leftArm4 = robot.getDevice('arm_left_4_joint')
rightArm4 = robot.getDevice('arm_right_4_joint')
leftArm4.setPosition(2.29)
rightArm4.setPosition(2.29)

leftMotor = robot.getDevice('wheel_left_joint')
rightMotor = robot.getDevice('wheel_right_joint')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)

braitenberg_coef=[]
for i in range(width):
  braitenberg_coef.append(gaussian(i, half_width, width/5))
  
left_obstacle = 0.0
right_obstacle = 0.0

while robot.step(timestep) != -1:
    lidar_values=lidar.getRangeImage()
    for i in range(int(half_width)):
      if (lidar_values[i] < range_threshold):  
        left_obstacle = left_obstacle + braitenberg_coef[i] * (1.0 - lidar_values[i] / max_range)
      #near obstacle sensed on the right side
      j = width - i - 1
      if (lidar_values[j] < range_threshold):
        right_obstacle = right_obstacle + braitenberg_coef[i] * (1.0 - lidar_values[j] / max_range)
    
    obstacle = left_obstacle + right_obstacle
    print('obstacle',obstacle,'right',right_obstacle,'left', left_obstacle)
    
    #compute the speed according to the information on obstacles
    if (left_obstacle > 0.55*obstacle):
      #speed_factor = (1.0 - DECREASE_FACTOR * obstacle) * MAX_SPEED / obstacle
      #print(speed_factor)
      left_speed = 15
      right_speed = -15
    elif(right_obstacle > 0.55*obstacle):
      left_speed = -15
      right_speed = 15
    elif(obstacle > THRESHOLD):
      s1=-1*(left_obstacle-THRESHOLD)/left_obstacle
      s2=-1*(right_obstacle-THRESHOLD)/right_obstacle
      left_speed = s1*5
      right_speed = s2*5
      
    else:
      left_speed = CRUISING_SPEED
      right_speed = CRUISING_SPEED
    
    #set actuators
    leftMotor.setVelocity(0.1*left_speed)
    rightMotor.setVelocity(0.1*right_speed)

    #reset dynamic variables to zero
    left_obstacle = 0.0
    right_obstacle = 0.0

