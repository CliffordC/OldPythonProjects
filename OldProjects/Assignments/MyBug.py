
from livewires import games, color
import random
from Goal import *
from Bug import *
from math import *

# Environmental inputs:
#   Am I bumping something?  self.bumping boolean
#   Where is the goal?       self.goal.x, self.goal.y

# Choose a next move by returning deltas for x and y
#   Move down and to the right:  (1, 1)
#   Move directly left:          (-1, 0)
#   Move up:                     (0, -1)
#   Go crazy:                    (1-2*random.random(), 1-2*random.random())

class MyBug(Bug):


    def setup(self):
        self.mode = "go to goal"
        self.move = (0,0)
        self.distance_to_goal = 0
        self.which_wall = "wall below"
        self.first_bump = (0,0)
        self.wall_movement = "check wall"
        self.closest_point = 0
        self.closest_position = (0,0)
        self.lap_counter = 0
        self.closest_point = hypot((self.goal.x - self.x),(self.goal.y - self.y))



    def choose_move(self):
        if self.x == self.first_bump[0] and self.y == self.first_bump[1]:
            self.lap_counter += 1
        if self.mode == "perimeter mode": #check for wall below
            print self.which_wall
            if self.which_wall == "check":
                self.move = (2,0)
                if self.bumping:
                    self.which_wall = "wall on right"
                    self.wall_movement = "move on wall"
                if not self.bumping:
                    self.which_wall = "wall below"
                    self.wall_movement = "move on wall"
                return self.move
            elif self.which_wall == "wall below": # move to the right on wall
                if self.wall_movement == "move on wall":
                    self.move = (2,0)
                    self.wall_movement = "check wall"
                    if not self.bumping:
                        self.which_wall = "wall on left"
                        self.wall_movement = "move on wall"
                        self.move = (-2,0)
                elif self.wall_movement == "check wall":
                    self.move = (0,2)
                    self.wall_movement = "move on wall"
                    if self.bumping:
                        self.which_wall = "wall on right"
            elif self.which_wall == "wall on left":
                if self.wall_movement == "move on wall":
                    self.move = (0,2)
                    self.wall_movement = "check wall"
                    if not self.bumping:
                        self.which_wall = "wall above"
                        self.wall_movement = "move on wall"
                        self.move = (0,-2)
                elif self.wall_movement == "check wall":
                    self.move = (-2,0)
                    self.wall_movement = "move on wall"
                    if self.bumping:
                        self.which_wall = "wall below"
            elif self.which_wall == "wall above": #move right on wall above
                if self.wall_movement == "move on wall":
                    self.move = (-2,0)
                    self.wall_movement = "check wall"
                    if not self.bumping:
                        self.which_wall = "wall on right"
                        self.wall_movement = "move on wall"
                        self.move = (2,0)
                elif self.wall_movement == "check wall":
                    self.move = (0,-2)
                    self.wall_movement = "move on wall"
            elif self.which_wall == "wall on right": #check for wall to the right
                #print "Here"
                if self.wall_movement == "move on wall":
                    print "moving"
                    self.move = (0,-2)
                    self.wall_movement = "check wall"
                    if not self.bumping:
                        self.which_wall = "wall below"
                        self.move = (2,0)
                elif self.wall_movement == "check wall":
                    print "checking"
                    self.move = (2,0)
                    self.wall_movement = "move on wall"
            if self.lap_counter > 1 and self.x == self.closest_position[0] and self.y == self.closest_position[1]:
                self.mode = "go to goal"
                self.lap_counter = 0
                #print self.x, "and ", self.y
        #movement towards the goal
        elif self.mode == "go to goal":  #if there is no wall keep moving
            if self.x > self.goal.x and  self.y > self.goal.y:
                self.move = (-2,-2)
            elif self.x > self.goal.x and self.y < self.goal.y:
                self.move = (-2, 2)
            elif self.x < self.goal.x and self.y > self.goal.y:
                self.move = (2,-2)
            elif self.x < self.goal.x and self.y < self.goal.y:
                self.move = (2, 2)
            elif self.x == self.goal.x or self.y == self.goal.y:
                if self.y > self.goal.y:
                    self.move = (0,-2)
                elif self.y < self.goal.y:
                    self.move = (0,2)
                elif self.x > self.goal.x:
                    self.move = (-2,0)
                elif self.x < self.goal.x:
                    self.move = (2,0)
        self.distance_to_goal = hypot((self.goal.x - self.x),(self.goal.y - self.y))
        if self.distance_to_goal < self.closest_point:
            self.closest_point =  self.distance_to_goal
            self.closest_position = (self.x, self.y)
            #print self.closest_position
        if self.bumping and self.lap_counter == 0:
            self.first_bump = (self.x, self.y)
            self.mode = "perimeter mode"
            self.which_wall = "check"
            #self.move = (0,1)
        return self.move













