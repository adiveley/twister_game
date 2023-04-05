""""A twister game written in python that allows multiple people to play twister"""


class Player:
    """One of the people playing the game"""
    
    def __init__(self, name):
        """Initializes a person object
        
        Args:
            name(str): the name of the player
            
        Side effects:
            Initializes attribute name
        """
            