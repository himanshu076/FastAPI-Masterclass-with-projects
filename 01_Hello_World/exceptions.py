# from fastapi 

class StoryException(Exception):
  def __ini__(self, name: str):
    self.name = name