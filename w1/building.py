class Room:

  def __init__(self: 'Room', name: str, sq: float):
    self.name = name
    self.square_footage = sq


class Building:

  def __init__(self: 'Building', address: str, rooms: list):
    self.address = address
    self.rooms = rooms

  def __repr__(self: 'Building') -> str:
    total = 0
    for room in self.rooms:
      total = total + room.square_footage
    return str(total)

  def rename(self: 'Building', old: 'str', new: str):
    for room in self.rooms:
      if room.name == old: # assuming rooms have unique names
        room.name = new
      

class BuildingCodeViolationError(Exception):
  pass


class House(Building):

  def __init__(self: 'House', address: str, rooms: list):
    if len(rooms) > 10:
      raise BuildingCodeViolationError    
    Building.__init__(self, address, rooms)
  
  def __repr__(self: 'House') -> str:
    result = 'Welcome to our house: \n'
    for room in self.rooms:
      result = result + room.name + ',' + str(room.square_footage) + '. '
    return result


class InvalidBusinessError(Exception):
  pass


class Business(Building):

  def __init__(self: 'Business', address: str, rooms: list):
    for room in rooms:
      if room.name == 'bedroom' or room.square_footage < 100:
        raise InvalidBusinessError
    Building.__init__(self, address, rooms)
  
  def rename(self: 'Business', old: 'str', new: str):
    if new == 'bedroom':
      raise InvalidBusinessError
    Building.rename(self, old, new)

  def change_sq(self: 'Business', existing: 'str', new_sq: float):
    if new_sq < 100:
      raise InvalidBusinessError
    for room in self.rooms:
      if room.name == existing:
        room.square_footage = new_sq


class BuildingCreationException(Exception):
  pass


if __name__ == "__main__":


# testing

  r1 = Room('Kitchen', 50)
  r2 = Room('Bathroom', 30)
  h = House('129 West 81st Street', [r1, r2])
  print(h)
  print()

  r3 = Room('Classroom', 300)
  b = Business('3359 Mississauga Road', [r3])
  print(b)
