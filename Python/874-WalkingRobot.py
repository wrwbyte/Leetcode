#Problem 874
#Solved in 36ms
#https://leetcode.com/problems/walking-robot-simulation/?envType=daily-question&envId=2026-04-06

#A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot receives an array of integers commands, which represents a sequence of moves that it needs to execute. There are only three possible types of instructions the robot can receive:
#     -2: Turn left 90 degrees.
#     -1: Turn right 90 degrees.
#     1 <= k <= 9: Move forward k units, one unit at a time.
# Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle, it will stay in its current location (on the block adjacent to the obstacle) and move onto the next command.
# Return the maximum squared Euclidean distance that the robot reaches at any point in its path (i.e. if the distance is 5, return 25).

#Approach:Check command and handle turning
#Attempt to move the robot to its final destination, then check if the robot would have hit an obstacle by checking a set of the obstacles (faster than looping through the list each time)
#If an obstacle is hit move to right before the obstacle (dependant on direction)
#Each time the piece is in a valid spot check if Max needs to be updated 
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        obstacles_set = set(map(tuple, obstacles))
        direction = 1 #1 is N, 2 is E, 3 is S, 4 is W
        pos = [0,0]
        maxd = 0
        for command in commands:
            if (command == -2): #TURN LEFT
                direction = direction-1
                if (direction == 0): direction = 4
            elif (command == -1): #TURN RIGHT
                direction = direction+1
                if (direction == 5): direction = 1
            else: #Intent to move
                if direction == 1: #north
                    start = pos[1]
                    pos[1] = pos[1]+command
                    for x in range(start+1,pos[1]+1): #Check if Obs
                        if (pos[0],x) in obstacles_set:
                            pos = [pos[0], x-1] #Hit the ob
                            break
                    if ((pos[0]**2 + pos[1]**2) >=maxd):
                            maxd = (pos[0]**2 + pos[1]**2)
                elif direction == 2: #east
                    start = pos[0]
                    pos[0] = pos[0]+command
                    for x in range(start+1,pos[0]+1): #Check if Obs
                        if (x,pos[1]) in obstacles_set:
                            pos = [x-1, pos[1]] #Hit the ob
                    if ((pos[0]**2 + pos[1]**2) >=maxd):
                            maxd = (pos[0]**2 + pos[1]**2)
                elif direction == 3: #south
                    start = pos[1]
                    pos[1] = pos[1]-command
                    for x in range(start-1, pos[1]-1, -1): #Check if Obs
                        if (pos[0],x) in obstacles_set:
                            pos = [pos[0], x+1] #Hit the ob
                    if ((pos[0]**2 + pos[1]**2) >=maxd):
                            maxd = (pos[0]**2 + pos[1]**2)
                elif direction == 4: #west
                    start = pos[0]
                    pos[0] = pos[0]-command
                    for x in range(start-1, pos[0]-1, -1): #Check if Obs
                        if (x,pos[1]) in obstacles_set:
                            pos = [x+1,pos[1]] #Hit the ob
                    if ((pos[0]**2 + pos[1]**2) >=maxd):
                            maxd = (pos[0]**2 + pos[1]**2)
        return maxd
