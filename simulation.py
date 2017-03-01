import math

from control import SLIDE_DIST_PER_STEP_IN
from control import ROTATE_DIST_PER_STEP_DEG

class Simulation:
  def __init__(self, control, center):
    self._tool_distance = 3
    self._tool_angle = 45
    self._center = center
    
    x = self._tool_distance * math.cos(math.radians(self._tool_angle))
    y = self._tool_distance * math.sin(math.radians(self._tool_angle))
    self._tool_path = [(self._center[0]+x,self._center[1]+y),]
    self._tool_pos = (self._center[0]+x,self._center[1]+y)
    
    self._control = control
    self._control.algorithm()

  def _calc_tool_pos(self):
    x = self._center[0]+(self._tool_distance * math.cos(math.radians(self._tool_angle)))
    y = self._center[1]+(self._tool_distance * math.sin(math.radians(self._tool_angle)))
    self._tool_path.append((x,y))
    self._tool_pos = (x,y)

  def _input(self, rotate, slide):
    if rotate > 0:
      self._tool_angle += ROTATE_DIST_PER_STEP_DEG
    elif rotate < 0:
      self._tool_angle -= ROTATE_DIST_PER_STEP_DEG
      
    if slide > 0:
      self._tool_distance += SLIDE_DIST_PER_STEP_IN
    elif slide < 0:
      self._tool_distance -= SLIDE_DIST_PER_STEP_IN 
    
  @property
  def center_axis(self):
    return self._center
    
  @property
  def tool_position(self):
    return self._tool_pos
   
  @property 
  def tool_history(self):
    return self._tool_path
    
  def step(self):
    cmd = self._control.get_command()
    self._input(cmd[0], cmd[1])
    self._calc_tool_pos()