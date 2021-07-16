from controller import Robot, Motor, DistanceSensor, Lidar

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = 64

MAX_SPEED = 6.28


lidar = robot.getDevice('Hokuyo URG-04LX-UG01')
lidar.enable(timestep)

#ds2 = robot.getDevice('ds2')
#ds2.enable(timestep)

#lidar = robot.getDevice('Hokuyo URG-04LX-UG01')
#lidar.enable(timestep)
#ds1 = robot.getDevice('ds1')
#ds1.enable(timestep)


while robot.step(timestep) != -1:
    val1=lidar.getRangeImage()
    #val2=ds2.getValue()
    
    print(val1)
