class Ship:

  '''Enemy ships.'''
  
  def __init__(self, hitpoints):
    '''(Ship, int)
    Create a Ship with given hitpoints at centre location.
    '''
    self.hitpoints = hitpoints
    self.location = 0
    
  def move_left(self):
    '''(Ship) -> NoneType
    Move Ship left.
      '''
    self.location -= 1
      
  def move_right(self):
    '''(Ship) -> NoneType
    Move Ship right.
      '''
    self.location += 1
      
  def get_hit(self, amount):
    '''(Ship, int) -> NoneType
    Get hit with an attack of amount.
    '''
    self.hitpoints -= amount

class IndestructibleShip(Ship):

  def get_hit(self, amount):
    '''(Ship, int) -> NoneType

    Get hit with an attack of amount.
    '''
    pass

