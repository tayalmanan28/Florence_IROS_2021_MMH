from controller import Robot, Motor, DistanceSensor, Lidar
import math

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = 64

MAX_SPEED = 6.28
CRUISING_SPEED = 5.0
OBSTACLE_THRESHOLD = 0.1
DECREASE_FACTOR = 0.9
BACK_SLOWDOWN = 0.9

def gaussian(x, mu, sigma):
  return (1.0 / (sigma * math.sqrt(6.28))) * math.exp(-((x - mu) * (x - mu)) / (2 * sigma * sigma))

lidar = robot.getDevice('Hokuyo URG-04LX-UG01')
lidar.enable(timestep)

width = lidar.getHorizontalResolution()
half_width=width/2
max_range = lidar.getMaxRange()
range_threshold = max_range / 20.0

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
    for i in range(half_width):
      if (lidar_values[i] < range_threshold):  
        left_obstacle = left_obstacle braitenberg_coefficients[i] * (1.0 - lidar_values[i] / max_range)
      #near obstacle sensed on the right side
      j = width - i - 1
      if (lidar_values[j] < range_threshold):
        right_obstacle = right_obstacle + braitenberg_coefficients[i] * (1.0 - lidar_values[j] / max_range)
    
    obstacle = left_obstacle + right_obstacle
    
    #compute the speed according to the information on obstacles
    if (obstacle > OBSTACLE_THRESHOLD):
      speed_factor = (1.0 - DECREASE_FACTOR * obstacle) * MAX_SPEED / obstacle
      left_speed = speed_factor * left_obstacle
      right_speed = speed_factor * right_obstacle
    else:
      left_speed = CRUISING_SPEED
      right_speed = CRUISING_SPEED
    
    #set actuators
    leftMotor.setVelocity(left_speed)
    rightMotor.setVelocity(right_speed)

    #reset dynamic variables to zero
    left_obstacle = 0.0
    right_obstacle = 0.0

