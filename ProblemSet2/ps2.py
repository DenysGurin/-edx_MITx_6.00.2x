# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import pylab

# For Python 2.7:
from ps2_verify_movement27 import testRobotMovement

# If you get a "Bad magic number" ImportError, you are not using 
# Python 2.7 and using most likely Python 2.6:


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        if width > 0 and height > 0:
            self.width = width
            self.height = height
            self.cleaned_list = []
        #raise NotImplementedError
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """

        cleaned_tile = (int(math.floor(pos.getX())),int(math.floor(pos.getY())))
        if cleaned_tile not in self.cleaned_list:        
            self.cleaned_list.append(cleaned_tile)

        
        #raise NotImplementedError

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        try:
            check_tile = (m, n)
            if check_tile in self.cleaned_list:   
                return True
            else:
                return False
        except AttributeError:
            return False
        #raise NotImplementedError
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height
        
        #raise NotImplementedError

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return len(self.cleaned_list)
        
        #raise NotImplementedError

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        return Position(random.uniform(0,self.width),random.uniform(0,self.height))
        #raise NotImplementedError

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        if pos.getX() < 0 or pos.getY() < 0:
            return False
        if pos.getX() >= self.width or pos.getY() >= self.height:
            return False
        return True
        
        #raise NotImplementedError
        
class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        #raise NotImplementedError

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        try:
            return self.POSITION 
        except AttributeError:
            self.POSITION = self.room.getRandomPosition()
            self.room.cleanTileAtPosition(self.POSITION)
            return self.POSITION 
        #raise NotImplementedError
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        try:
            return self.DIRECTION
        except AttributeError:
            self.DIRECTION = random.uniform(0,360)
            return self.DIRECTION
        #raise NotImplementedError

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        if self.room.isPositionInRoom(position):
            self.POSITION = position
        #raise NotImplementedError

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.DIRECTION = direction
        #raise NotImplementedError

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        
        raise NotImplementedError # don't change this!

# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
        
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        try:
            try:
                self.POSITION
            except AttributeError:
                StandardRobot.getRobotPosition(self)  
            
            
            self.new_POSITION = self.POSITION.getNewPosition(self.DIRECTION, self.speed)
            if self.room.isPositionInRoom(self.new_POSITION):
                self.POSITION = self.new_POSITION
                
            else:
                while not self.room.isPositionInRoom(self.new_POSITION):
                    self.DIRECTION = random.uniform(0,360)
                    self.new_POSITION = self.POSITION.getNewPosition(self.DIRECTION, self.speed)
                self.POSITION = self.new_POSITION
            if not self.room.isTileCleaned(int(self.POSITION.getX()), int(self.POSITION.getY())):
                    self.room.cleanTileAtPosition(self.POSITION)
        except AttributeError: 
            StandardRobot.getRobotDirection(self)

# Uncomment this line to see your implementation of StandardRobot in action!
#testRobotMovement(StandardRobot, RectangularRoom)

#position = Position(1,1)
#print position.getX()
#print position.getY()
#room = RectangularRoom(3,3)
##robot = Robot(room, 1.0)
##robot.getRobotPosition()
##print robot.getRobotPosition()
##robot.setRobotPosition(position)
##robot.setRobotDirection(20)
##print robot.getRobotPosition()
##print robot.getRobotDirection()
#
#walking_robot = StandardRobot(room, 1.0)
##walking_robot.updatePositionAndClean()
#print "start position :"
#for i in range(10):
#    walking_robot.updatePositionAndClean()
#    print walking_robot.getRobotPosition()

#avg = runSimulation(10, 1.0, 15, 20, 0.8, 30, StandardRobot)
# === Problem 3
def runSimulation(num_robots=10, speed=1.0, width=15, height=20, min_coverage=0.8, num_trials=30,
                  robot_type=StandardRobot):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    mean_steps = 0
    list_rooms = []
    list_robots = []
    list_trials = []
    list_steps = []
    
    """for room in range(num_trials): #add room object to 'list_rooms'
        list_rooms.append(RectangularRoom(width, height))"""
    for trial in range(num_trials): #add robot object to 'list_robots' and fillup 'list_trials'
        list_rooms.append(RectangularRoom(width, height))
        list_trials.append([])
        for robot in range(num_robots):
            #list_robots.append(robot_type(list_rooms[trial], speed)) #robot object to 'list_robots'
            list_trials[trial].append(robot_type(list_rooms[trial], speed)) #robot object to 'list_trials[trial]'
        steps = 0
        while int(list_rooms[trial].getNumTiles()*min_coverage) >= list_rooms[trial].getNumCleanedTiles():
            steps += 1
            for robot in list_trials[trial]:
                robot.updatePositionAndClean()
                
                #print robot, robot.getRobotPosition(), list_rooms[trial].getNumCleanedTiles()
        
        list_steps.append(steps)
    """for trial in range(num_trials): #run simulation for each 'trial' in 'trial_list'
        steps = 0
        while int(list_rooms[trial].getNumTiles()*min_coverage) != int(list_rooms[trial].getNumCleanedTiles()*min_coverage):
            steps += 1
            for robot in list_trials[trial]:
                robot.updatePositionAndClean()
                
                #print robot, robot.getRobotPosition(), list_rooms[trial].getNumCleanedTiles()
        
        list_steps.append(steps)"""
    """
    print "list_rooms",  list_rooms, len(list_rooms)
    print "list_robots",  list_robots, len(list_robots)
    print "list_trials",  list_trials, len(list_trials)
    print "list_steps", list_steps, len(list_steps)
    """
    mean_steps = sum(list_steps)/len(list_steps)
    
    return mean_steps

# Uncomment this line to see how much your simulation takes on average
print  runSimulation(10, 1.0, 10, 10, 0.75, 30, StandardRobot)
#runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot)

# === Problem 4
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """           
        try:
            try:
                self.POSITION
            except AttributeError:
                RandomWalkRobot.getRobotPosition(self)
            self.DIRECTION
        except AttributeError:
            RandomWalkRobot.getRobotDirection(self)
            
        self.new_POSITION = self.POSITION.getNewPosition(RandomWalkRobot.getNewDirection(self), self.speed)
        while not self.room.isPositionInRoom(self.new_POSITION):
            self.DIRECTION = RandomWalkRobot.getNewDirection(self)
            self.new_POSITION = self.POSITION.getNewPosition(self.DIRECTION, self.speed)
        self.POSITION = self.new_POSITION
        if not self.room.isTileCleaned(int(self.POSITION.getX()), int(self.POSITION.getY())):
                    self.room.cleanTileAtPosition(self.POSITION)

    def getNewDirection(self):
            self.DIRECTION = random.uniform(0,360)
            return self.DIRECTION
# Uncomment this line to see your implementation of StandardRobot in action!
#testRobotMovement(RandomWalkRobot, RectangularRoom)
def visualization():
    width = 10
    height = 20
    room = RectangularRoom(width,height)
    robots = [RandomWalkRobot(room, 1.0), RandomWalkRobot(room, 1.0), StandardRobot(room, 1.0), StandardRobot(room, 1.0)]
    num_robots = len(robots)
    
    anim = ps2_visualize.RobotVisualization(num_robots, width, height)
    #anim.update(room, robots)
    while room.getNumTiles() != room.getNumCleanedTiles():
        for robot in robots:
            robot.updatePositionAndClean() 
        anim.update(room, robots)                
    anim.done()
    

                                                                                                                                          
def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print "Plotting", num_robots, "robots..."
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300/width
        print "Plotting cleaning time for a room of width:", width, "by height:", height
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
    
visualization()
showPlot1('sad','sad','sad')
showPlot2('sad','sad','sad')
# === Problem 5
#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#
