# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name, current_room, inventory = None):
    self.name = name
    self.current_room = current_room
    self.inventory = [] if inventory is None else inventory

  # def grab(self, item):
  #   print(self.current_room.inventory)

  # def drop(self, item):
  #   print(self.current_room.inventory)