class Base:
    """The class Base"""
    
    __nb_objects = 0
    """private class attribute"""
    
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            __nb_objects += id
            