# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
  def __init__(self, name, desc, inventory = None):
    self.name = name
    self.desc = desc
    # self.inventory = [] if inventory is None else inventory
    if inventory == None:
      self.inventory = []
    else:
      self.inventory = inventory