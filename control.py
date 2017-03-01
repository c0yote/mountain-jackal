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
    # This test will make the machine step 25x50 step "rectangle" 
    # Slide Outboard
    for i in range(60):
      self.put_command(0,1)
    # Rotate Clockwise
    for i in range(25):
      self.put_command(1,0)
    # Slide Inboard
    for i in range(60):
      self.put_command(0,-1)
    # Rotate Counter-Clockwise
    for i in range(25):
      self.put_command(-1,0)
      
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# THESE CONSTANTS MAY NEED CHANGED
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
PIXELS_PER_INCH = 10
SLIDE_DIST_PER_STEP_IN = .05
ROTATE_DIST_PER_STEP_DEG = .9