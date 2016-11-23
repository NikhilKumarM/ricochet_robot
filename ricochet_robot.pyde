
# ---------- My Code Nikhil Kumar Mengani ----------
# please define the path of test file 
path_to_file_containing_puzzle = "Path_to_input_file"
    
def cost(s,g,dir):
       (x1,y1)=s;
       (x2,y2)=dir;
       (x3,y3)=g;     
       #calculating the distance
       distance=abs(x2-x1)+abs(y2-y1)+abs(x3-x2)+abs(y3-y2)
       return distance
# finding manhatton distance   
def mandist(s,g):
       (x1,y1)=s;
       (x2,y2)=g;
       #calculating the distance
       distance=abs(x2-x1)+abs(y2-y1)
        
       return distance 
# finding Heuristic distance     
def heuristic(g,dir):
       (x1,y1)=g;
       (x2,y2)=dir;
            #calculating the distance
       hdistance=abs(x2-x1)+abs(y2-y1)
        
       return hdistance   
# finding the cost to reach the node to expanded
def prevcost(minkey):
    s1=0
    s2=0
    s=(s1,s2)
    dis=0
    i=0
    for t in minkey: 
         if(i==0):
              s=t    
         dis=dis+mandist(s,t)
         s=t
         i+=1
    return dis
   
   
    
def solve():
    """This method should compute and return the solution, as a list
    of (row, column) tuples, zero-based. What it currently does is
    just provide a hand-crafted solution.
    """
    s=ball_location
    g=goal_location
    # Using the functions UP,DOWN, LEFT,RIGHT for directions..that are declared after solve functions
    up=UP(s)  
    down=DOWN(s)
    left= LEFT(s)
    right=RIGHT(s)
    dict={};
    dict1={}
    dict[(s,up)]=cost(s,g,up);
    dict[(s,down)]=cost(s,g,down)
    dict[(s,left)]=cost(s,g,left)
    dict[(s,right)]=cost(s,g,right)
    # defining the recursive function to get path to goal state
    def goal(dict,dict1,s,g):
             if(not bool(dict)):
                 raise ValueError("NO SOLUTION");
             minkey=min(dict,key=dict.get);
             nodetoexp=minkey[len(minkey)-1]
             if(nodetoexp in dict1.keys() and dict1[nodetoexp]<dict[minkey]):
                        del dict[minkey]
             #if(noetoexp in dict1.keys() and dict1[nodetoexp]>dict[minkey]):                   
             #           dict1[nodetoexp]=dict[minkey]''' 
             else:              
               dict1[nodetoexp]=dict[minkey]
               (lr,lc)=minkey[len(minkey)-1]
               (lbr,lbc)=minkey[len(minkey)-2]
               if(lr==lbr):
                  op1=UP(nodetoexp)
                  op2=DOWN(nodetoexp)
               if(lc==lbc):
                  op1=LEFT(nodetoexp)
                  op2=RIGHT(nodetoexp)
               del dict[minkey]
               temp=minkey;     
               minkey=list(minkey)
               temp=list(temp)
               minkey.append(op1);
               temp.append(op2);
               minkey=tuple(minkey);
               temp=tuple(temp)
               dict[minkey]=heuristic(op1,g)+prevcost(minkey)
               dict[temp]=heuristic(op2,g)+prevcost(temp)
               if(op1==g ):
            
                   return list(minkey)
           
               if(op2==g):
                  return list(temp)
               if(op1==nodetoexp):
                    del dict[minkey]
               if(op2==nodetoexp and temp in dict.keys()):
                   del  dict[temp]                
             sol=goal(dict,dict1,s,g)    
             return sol
         
    return  goal(dict,dict1,s,g)  
#----------------------------------------------------------------------------------------------
#--------------------------- UP,DOWN,RIGHT,LEFT functions--------------------------------------    
def UP((r,c)):
     up=(r,c)
     while (up not in block_locations and  r < number_of_rows and r>=0):
          r-=1;
          up= (r,c);
          if(up==goal_location):
              return up
     #if(up in block_locations or r <0):
     r+=1
     up=(r,c)
     return up
def DOWN((r,c)):
    down=(r,c)
    while(down not in block_locations and  (r <number_of_rows and r>=0)):
          r+=1
          down= (r,c)
          if(down==goal_location):
              return down
    # if(down in block_locations or r >number_of_rows):
    r-=1
    down=(r,c)
    return down;   
def RIGHT((r,c)):
    right=(r,c)
    while(right not in block_locations and  (c < number_of_columns and c>=0)):
          c+=1
          right= (r,c)
          if(right==goal_location):
              return right
    
    #if(right in block_locations or c > number_of_columns):
    c-=1
    right=(r,c)
    
    return right      
    
def LEFT((r,c)):
    left=(r,c)   
    while(left not in block_locations and  (c < number_of_columns and c>=0)):
          c-=1
          left=(r,c)
          if(left==goal_location):
              return left
          
    #if(left in block_locations or c <0):
    c+=1
    left=(r,c)
    return left 

     
               
# I HAVE NOT WRITTEN THIS FOLLOWING LINES OF CODE . THE FOLLOWING CODE IS GIVEN AND I HAVE WRITTEN THE ABOVE LINES OF CODE TO FIND SHORTEST PATH  
# -------------------------------------------------------------------------
# ----- The following code provides the GUI and should not be altered -----
    
def setup():
    """This method is called automatically once, when program starts.
    """
    global game
    size(300, 300) # arguments _must_ be literal integers, not variables!!!
    read_puzzle(path_to_file_containing_puzzle)
    game = Ricochet(number_of_rows, number_of_columns)
    game.place_blocks(block_locations)
    game.place_ball(ball_location)
    game.place_goal(goal_location)
    solution = solve()
    game.set_path(solution)
    
def draw():
    """This method is called automatically 60 times a second.
    Its job is to draw everything.
    """
    background(255)
    game.draw_grid(game.rows, game.columns)
    game.draw_blocks()
    game.draw_goal()
    game.draw_ball()
    game.move_ball()

def read_puzzle(file_path):
    """Read in a ricochet puzzle, putting results in global variables.
    Values must be one per line, in the given order. Comments,
    indicated with a # character, may occur after the value."""
    global number_of_rows, number_of_columns, block_locations
    global ball_location, goal_location
    file = open(file_path, "r")
    number_of_rows =    read_and_evaluate_line(file)
    number_of_columns = read_and_evaluate_line(file)
    block_locations =   read_and_evaluate_line(file)
    ball_location =     read_and_evaluate_line(file)
    goal_location =     read_and_evaluate_line(file)
    file.close()

def read_and_evaluate_line(file):
    line = file.readline()
    data = eliminate_comment(line)
    return eval(data)
    
def eliminate_comment(line):
    """Removes the # character (if there is one) and everything after it."""
    hash_at = line.find("#")
    if hash_at >= 0:
        return line[:hash_at]
    else:
        return line
class Ricochet:
    """This defines the display for the game. To use this display,
    create a "ricochet object" with
        game = ricochet(number of rows, number of columns)
    then call any or all of the methods
      * game.place_ball(row, column)
      * game.place_goal(row, column)
      * game.place_blocks( a list of (row, column) tuples )
      * game.set_path( a list of (row, column) tuples )
    """    
    
    def __init__(self, number_of_rows, number_of_columns):
        """This method is automatically called when you say
            game = ricochet(number of rows, number of columns)
        and should never be called explicitly. It contains a
        few constants you may wish to modify.
        """
        self.cell_size = min(width // (number_of_columns + 2),
                        height // (number_of_rows + 2))
        self.x = self.cell_size           # position of left edge of grid
        self.y = self.cell_size           # position of top edge of grid
        self.rows = number_of_rows
        self.columns = number_of_columns
        self.block_locations = []         # to be filled in
        self.path = []                    # to be filled in
        self.ball_x_y_position = (-1, -1) # to be replaced
        self.goal_location = -1           # leave alone!
        self.initial_delay = 60           # delay before ball starts to move
        ellipseMode(CORNER)
        strokeCap(ROUND)
    
    def place_ball(self, location):
        """Specifies the initial location of the red ball."""
        self.ball_x_y_position = self.row_column_to_x_y(location)
        
    def place_goal(self, location):
        """Specifies the location of the goal cell (green X)."""
        self.goal_location = location
        
    def place_blocks(self, locations):
        """Given any number of (row, column) tuples, place blocks at
           those locations. Previous blocks, if any, are forgotten.
           """
        self.block_locations = list(locations)
        
    def set_path(self, locations):
        """Given a list of (row, column) tuples, define a path
        for the red ball to follow, starting from where it has been
        placed initially. The ball will move to each location in
        turn.
        This method does NOT test whether the path is legal; it
        will simply move the ball where it is told to.
        """
        self.path = list(locations)
        self.path_index = -1 # used to keep track of red ball moves
        
    def move_ball(self):
        """Given a list of (row, column) tuples, define a path
        for the red ball to follow, starting from its current
        location. The ball will move to each location in turn.
        
        This method does NOT test whether the path is legal; it
        will simply move the ball where it is told to, even
        diagonally, through blocks, or off the screen.
        """
        if self.initial_delay > 0:
            self.initial_delay -= 1
            return # Pause before ball starts to move
        if self.path_index == -1 :
            self.path_index = 0
            return # Just starting the path
        if self.path_index >= len(self.path):
            noLoop()
            return # reached end of path
        elif self.ball_x_y_position == \
             self.row_column_to_x_y(self.path[self.path_index]):
            self.path_index += 1
            return # reached one location, ready to move to next location
        else:
            self.move_ball_toward(self.path[self.path_index])
            return # moved slightly closer to next desired location
                        
    def draw_grid(self, rows, columns):
        """Draw a rows x columns grid starting at (x, y)."""
        size = self.cell_size
        x = size
        y = size
        stroke(0)
        strokeWeight(1)
        if rows > 0:
            h_length = size * columns
            v_length = size * rows
            for i in range (0, rows + 1):
                line(x, y + i * size, x + h_length, y + i * size)
            for i in range (0, columns + 1):
                line(x + i * size, y, x + i * size, y + v_length)
        
    def draw_blocks(self):
        """Draws a black square at every location in block_locations."""
        fill(0)
        for location in self.block_locations:
            (x, y) = self.row_column_to_x_y(location)
            rect(x, y, self.cell_size, self.cell_size)
           
    def draw_ball(self):
        """Draws the red ball at the position indicated by
        ball_x_y_position, which is not necessarily exactly
        within a single cell.
        """
        fill(255, 0, 0)
        noStroke()
        (x, y) = self.ball_x_y_position
        ellipse(x + 2, y + 2, self.cell_size - 3, self.cell_size - 3)
        
    def draw_goal(self):
        """Draws a green X at goal_location."""
        stroke(0, 255, 0)
        strokeWeight(2)
        (x, y) = self.row_column_to_x_y(self.goal_location)
        line(x, y, x + self.cell_size, y + self.cell_size)
        line(x, y + self.cell_size, x + self.cell_size, y)
        
    def move_ball_toward(self, new_location):
        """Adjust the current (x, y) position of the red ball to be
        slightly closer to the new location, given as (row, column)."""
        (old_x, old_y) = self.ball_x_y_position
        (new_x, new_y) = self.row_column_to_x_y(new_location)
        self.ball_x_y_position = (self.toward(old_x, new_x),
                                  self.toward(old_y, new_y))
        
    def toward(self, frum, to): # "from" is a reserved word
        """Return one of the values frum-1, frum, or frum+1,
        whichever is closer to 'to'."""
        if frum < to: return frum + 1
        elif frum > to: return frum - 1
        else: return frum
    
    def row_column_to_x_y(self, location):
        """Convert a (row, column) tuple to the (x, y) coordinates of
        the top left corner of the cell at that location."""
        (row, column) = location
        return (self.x + column * self.cell_size, self.y + row * self.cell_size)