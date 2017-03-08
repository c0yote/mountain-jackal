import datetime
import math

class Control:
  def __init__(self):
    self._cmd_queue = []
  
  def put_command(self, rotate, slide):
    self._cmd_queue.append([rotate, slide])
  
  def get_command(self):
    if len(self._cmd_queue) < 1:
      return (0,0)
    else:
      return self._cmd_queue.pop(0)
      
  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  # THIS FUNCTION IS WHERE YOU WORK
  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  def algorithm(self):
    
    ###
    #  Written for human consumption and understanding, not efficiency.
    ###
  
    def dist_between(p_a, p_b):
      return math.sqrt(math.pow(p_a[0]-p_b[0], 2) + math.pow(p_a[1]-p_b[1], 2))
  
    def dist_from_line(lp_a, lp_b, p):
      # This function does not work for lines directly on the X or Y axis.
      #
      # (|(y2-y1)x0 - (x2-x1)y0 + x2y1 - y2x1|) / √((y2-y1)^2 + (x2-x1)^2)
      x0 = p[0]       # A point off the line.
      y0 = p[1]       #  ...
      x1 = lp_a[0]    # A point on line the line.
      y1 = lp_a[1]    #  ...
      x2 = lp_b[0]    # Another point on line the line.
      y2 = lp_b[1]    #  ...
      
      # d = (|(y2-y1)x0 - (x2-x1)y0 + x2y1 - y2x1|) / √((y2-y1)^2 + (x2-x1)^2)      
      dividend  = abs((y2-y1)*x0-(x2-x1)*y0+x2*y1-y2*x1)
      divisor = math.sqrt(math.pow(y2-y1,2) + math.pow(x2-x1,2))      
      return dividend / divisor
    
    def to_polar(point):
      return (
        math.sqrt(math.pow(point[0], 2)+math.pow(point[1], 2)),       # r
        math.degrees(math.atan2(point[1],point[0])))                  # theta
    
    def to_carte(point):
      return (
        point[0] * math.cos(math.radians(point[1])),                  # x
        point[0] * math.sin(math.radians(point[1])))                  # y
  
    def traverse(start_point, target_point, speed_fps=None):
      tool_point = start_point # Assume tool is at the start_point and store it.
      tool_polar = to_polar(tool_point)
      start_polar = to_polar(start_point)
      target_polar = to_polar(target_point)
      
      while True:
        action = None
        dist_off_line = 999999 # Just need an impossibly high number.
        dist_to_target = dist_between(tool_point, target_point)
        theory_point = None
        tool_polar = to_polar(tool_point)
        
        # Decide which movement possibilities are applicable based on r and theta,
        #  of both the start and target points. (You wouldn't move AWAY from the 
        #  target so it must be the other way.)
        #  Next decide which action to take based on which one stays closest
        #  to the line between the start and target points.
        
        # Extension\Contraction theory.
        if start_polar[0] < target_polar[0]:    # Arm will need to extend.
          theory_point = to_carte((tool_polar[0]+SLIDE_DIST_PER_STEP_IN, tool_polar[1]))
          temp_to_target = dist_between(theory_point, target_point)
          temp_from_line = dist_from_line(start_point, target_point, theory_point)
          # Check we are closing on target and this option is closest to line.
          if temp_to_target < dist_to_target and temp_from_line < dist_off_line:
            dist_off_line = temp_from_line         # Store because no alternative.
            action = 'extend'                      # Set action, for now.
        else:                                   # Arm will need to contract.
          theory_point = to_carte((tool_polar[0]-SLIDE_DIST_PER_STEP_IN, tool_polar[1]))
          temp_to_target = dist_between(theory_point, target_point)
          temp_from_line = dist_from_line(start_point, target_point, theory_point)
          # Check we are closing on target and this option is closest to line.
          if temp_to_target < dist_to_target and temp_from_line < dist_off_line:
            dist_off_line = temp_from_line         # Store because no alternative.
            action = 'contract'                    # Set action, for now.
        
        # Rotation theory.
        if start_polar[1] < target_polar[1]:    # Arm will need to rotate CCW.
          theory_point = to_carte((tool_polar[0], tool_polar[1]+ROTATE_DIST_PER_STEP_DEG))
          temp_to_target = dist_between(theory_point, target_point)
          temp_from_line = dist_from_line(start_point, target_point, theory_point)
          # Check we are closing on target and this option is closest to line.
          if temp_to_target < dist_to_target and temp_from_line < dist_off_line:
            dist_off_line = temp_from_line         # Store because no alternative.
            action = 'ccw'                         # Set action, for now.
        else:                                   # Arm will need to rotate CW.
          theory_point = to_carte((tool_polar[0], tool_polar[1]-ROTATE_DIST_PER_STEP_DEG))
          temp_to_target = dist_between(theory_point, target_point)
          temp_from_line = dist_from_line(start_point, target_point, theory_point)
          # Check we are closing on target and this option is closest to line.
          if temp_to_target < dist_to_target and temp_from_line < dist_off_line:
            dist_off_line = temp_from_line         # Store because no alternative.
            action = 'cw'                          # Set action, for now.
            
        # Depending on kerf you could add other options here like combination movements.
        
        # Take action
        if action is None:          # Tool as close as it will ever get.
          print('exit')
          break;                      # Break out of action loop.
        elif action == 'extend':    # Extend was closest to path.
          action_point = to_carte((tool_polar[0]+SLIDE_DIST_PER_STEP_IN, tool_polar[1]))
          action_dist_taken = dist_between(tool_point, target_point)
          tool_point = action_point
          self.put_command(0,1)
        elif action == 'contract':  # Contract was closest to path.
          action_point = to_carte((tool_polar[0]-SLIDE_DIST_PER_STEP_IN, tool_polar[1]))
          action_dist_taken = dist_between(tool_point, target_point)
          tool_point = action_point
          self.put_command(0,-1)
        elif action == 'ccw':       # Counter Clockwise was closest to path.
          action_point = to_carte((tool_polar[0], tool_polar[1]+ROTATE_DIST_PER_STEP_DEG))
          action_dist_taken = dist_between(tool_point, target_point)
          tool_point = action_point
          self.put_command(1,0)
        elif action == 'cw':        # Clockwise was closest to path.
          action_point = to_carte((tool_polar[0], tool_polar[1]-ROTATE_DIST_PER_STEP_DEG))
          action_dist_taken = dist_between(tool_point, target_point)
          tool_point = action_point
          self.put_command(-1,0)
        else:
          print('error')
    
        # Hanger on for speed control.
        action_taken_time = datetime.datetime.now()
        #print(action_dist_taken)

        
    # Test Scenarios
    def test_square():  # Usage Test - square
      start_point = to_carte((TOOL_START_DIST_IN,TOOL_START_ANGLE_DEG))
      point_1 = (4,7)
      point_2 = (7,7)
      point_3 = (7,4)
      traverse(start_point, point_1)
      traverse(point_1, point_2)
      traverse(point_2, point_3)
      traverse(point_3, start_point)
    
    def test_long_line_bad_angle(): # Usage Test - long line
      start_point = to_carte((TOOL_START_DIST_IN,TOOL_START_ANGLE_DEG))
      point_1 = (23,6)
      traverse(start_point, point_1)
    
    def test_big_catywompus_square(): # Usage Test - Catywompus Square
      start_point = to_carte((TOOL_START_DIST_IN,TOOL_START_ANGLE_DEG))
      point_1 = (7,27)
      point_2 = (30,25)
      point_3 = (27,2)
      traverse(start_point, point_1)
      traverse(point_1, point_2)
      traverse(point_2, point_3)
      traverse(point_3, start_point)
      
    def test_arc_bug():
      start_point = to_carte((TOOL_START_DIST_IN,TOOL_START_ANGLE_DEG))
      point_1 = (-5,7)
      point_2 = (-5,12)
      point_3 = (12,12)
      traverse(start_point, point_1)
      traverse(point_1, point_2)
      traverse(point_2, point_3)
      traverse(point_3, start_point)
    
    # Test Run
    test_big_catywompus_square()
    #test_arc_bug()
    #test_square()
    #test_long_line_bad_angle()

      
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# THESE CONSTANTS MAY NEED CHANGED
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
FEED_SPEED_FPS = .167
PIXELS_PER_INCH = 10
SLIDE_DIST_PER_STEP_IN = .05
ROTATE_DIST_PER_STEP_DEG = .45
TOOL_START_DIST_IN = 5.6568542494924
TOOL_START_ANGLE_DEG = 45
