# ricochet_robot
GOAL:
Making the robot move from starting position to goal position without colliding with the blocks , in the shortest path. 

HOW TO RUN:
In the ricochet_robot.pyde file set ->   path_to_file_containing_puzzle = "Path_to_input_file".

Input file(.txt) should have following format:

8 # Number of rows
8 # Number of columns
[(0, 4), (1, 1), (2, 5), (4, 4), (4, 7), (5, 0), (6, 2), (7, 6)]  # List of block locations
(6,4) # Where the ball starts
(2,4) # Goal location 
