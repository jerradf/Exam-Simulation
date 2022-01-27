# md.py
# Jerrad Flores

# Continously tracks the location of the mouse in
# the areas of the exam window.
# If the mouse moves to a completely different
# location than where it was last detected,
# we can suspect that the user is going to another 
# window and searching for answers to the exam (or 
# other forms of cheating).


class MouseDetector(): 

  def __init__(self):
    self.x = 0
    self.y = 0
    self.mouse_movements = []


  def detect_warnings(self, x, y):
    warning1 = bool
    warning2 = bool
    warning3 = bool
    warning4 = bool

    if self.x != 0 and self.y != 0:
      # Rapid Movements
      if ((self.x - x) > 225) or ((x - self.x) > 225):
        self.mouse_movements.append("Warning-1")
        warning1 = True
      if ((self.y - y) > 225) or ((y - self.y) > 225):
        warning2 = True
        self.mouse_movements.append("Warning-2")
      # Out-of-bounds
      if x >= 448 or x <= 4:
        warning3 = True
        self.mouse_movements.append("Warning-3")
      if y >= 411 or y <= 4:
        warning4 = True
        self.mouse_movements.append("Warning-4")
    self.x, self.y = (x, y)

    # 2 Boundary Movements at the same time.
    if warning3 == True and warning4 == True:
      return True
    elif warning1 == True and warning2 == True:
      return True
    elif warning2 == True and warning3 == True:
      return True
    elif warning1 == True and warning3 == True:
      return True
    elif warning1 == True and warning4 == True:
      return True
    elif warning2 == True and warning4 == True:
      return True
    elif warning2 == True and warning3 == True and warning4 == True:
      return True
    elif warning1 == True and warning2 == True and warning3 == True:
      return True
    elif warning1 == True and warning3 == True and warning4 == True:
      return True
    elif warning1 == True and warning2 == True and warning4 == True:
      return True
    else:
      return False


  def detector(self, event):
    self.mouse_movements.append((event.x, event.y))
    return self.detect_warnings(event.x, event.y)