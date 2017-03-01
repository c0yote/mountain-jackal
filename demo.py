from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.widget import Widget

def simulate():
  return 1
  
class Simulation:
  def __init__(self):
    self.sim_time = 0
  
  def step(self, dt):
    self.sim_time += 1
    print(self.sim_time)
    return (self.sim_time, self.sim_time)

class PlateWidget(Widget):
  def setup_simulation(self):
    self.sim = Simulation()

  def cut(self, dt):
    with self.canvas:
      Color(1, 1, 0)
      Ellipse(pos=self.sim.step(1), size=(2, 2))
  
class DemoApp(App):
  def build(self):
    w = PlateWidget()
    w.setup_simulation()
    
    event = Clock.schedule_interval(w.cut, 1 / 60.)
    
    return w
    
if __name__ == '__main__':
    DemoApp().run()