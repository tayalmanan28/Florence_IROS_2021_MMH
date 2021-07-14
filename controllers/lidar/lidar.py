"""lidar controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, DistanceSensor

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = 64

MAX_SPEED = 6.28

ds = []
dsNames = [
    'ds1', 'ds2', 'ds3', 'ds4',
    'ds5', 'ds6', 'ds7', 'ds8'
]

for i in range(8):
    ds.append(robot.getDevice(dsNames[i]))
    ds[i].enable(timestep)

leftMotor = robot.getDevice('wheel_left_joint')
rightMotor = robot.getDevice('wheel_right_joint')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)

#lidar = robot.getDevice('Hokuyo URG-04LX-UG01')
#lidar.enable(timestep)
#ds1 = robot.getDevice('ds1')
#ds1.enable(timestep)


while robot.step(timestep) != -1:
    dsValues = []
    for i in range(8):
        dsValues.append(ds[i].getValue())

    # detect obstacles
    right_obstacle = dsValues[0] > 80.0 or dsValues[1] > 80.0 or dsValues[2] > 80.0
    left_obstacle = dsValues[5] > 80.0 or dsValues[6] > 80.0 or dsValues[7] > 80.0

    # initialize motor speeds at 50% of MAX_SPEED.
    leftSpeed  = 0.5 * MAX_SPEED
    rightSpeed = 0.5 * MAX_SPEED
    # modify speeds according to obstacles
    if left_obstacle:
        # turn right
        leftSpeed  = 0.5 * MAX_SPEED
        rightSpeed = -0.5 * MAX_SPEED
    elif right_obstacle:
        # turn left
        leftSpeed  = -0.5 * MAX_SPEED
        rightSpeed = 0.5 * MAX_SPEED
    # write actuators inputs
    leftMotor.setVelocity(leftSpeed)
    rightMotor.setVelocity(rightSpeed)
    pass

# Enter here exit cleanup code.
