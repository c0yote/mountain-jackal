from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.widget import Widget

from control import Control
from simulation import Simulation

from control import PIXELS_PER_INCH
  
class PlateWidget(Widget):
  def setup_simulation(self):
    self.sim = Simulation(Control(), (0,0))

  def render(self, dt):
    with self.canvas:
      self.sim.step()
      self.canvas.clear()    
      Color(.5, .5, .5)
      x = (self.sim.center_axis[0] * PIXELS_PER_INCH)+400-4
      y = (self.sim.center_axis[1] * PIXELS_PER_INCH)+300-4
      Ellipse(pos=(x,y), size=(9, 9))
   
      Color(1, 1, 0)
      for p in self.sim.tool_history:
        x = ((p[0]*1) * PIXELS_PER_INCH)+400-1
        y = ((p[1]*1) * PIXELS_PER_INCH)+300-1
        Ellipse(pos=(x,y), size=(3, 3))
        
      Color(1,0,0)
      x = (self.sim.tool_position[0] * PIXELS_PER_INCH)+400-2
      y = (self.sim.tool_position[1] * PIXELS_PER_INCH)+300-2
      Ellipse(pos=(x,y), size=(5, 5))
  
class DemoApp(App):
  def build(self):
    w = PlateWidget()
    w.setup_simulation()
    
    # Schedule simulation step
    event = Clock.schedule_interval(w.render, 1 / 60.)
    
    return w
    
if __name__ == '__main__':
    DemoApp().run()