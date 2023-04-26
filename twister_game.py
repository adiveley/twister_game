""""A twister game written in python that allows multiple people to play twister"""
import random

class Player:
    """One of the people playing the game
    
    Attributes:
        name(str): The name of the player
        right_foot(int): A number(1) that represents the right foot
        left_foot(int): A number(2) that represents the left foot
        right_hand(int): A number(3) that represents the right hand
        left_hand(int): A number(4) that represents the left hand"""
        
    
    
    def __init__(self, name, right_foot, left_foot, right_hand = 0, left_hand = 0):
        """Initializes a person object. Uses optional parameters.
        
        Args:
            name(str): the name of the player
            
        Side effects:
            Initializes attribute name,right_foot,left_foot,right_hand,left_hand
        """
        self.spinner_colors = ["green", "yellow", "blue", "red", "spinner_choice"]
        self.spinner_body_parts = ["right_foot", "left_foot", "right_hand", "left_hand", "spinner_choice"]
        
    def turn(self,name):
        """Executes a player turn. Uses sequence unpacking.
        
        Args:
            name(str): Name of the current player
        Raises:
            ValueError: body part and color selected are not found within the spinnner_color or spinner_body_parts
        Side effects:
            Prompts the current player to spin for a body part and a color.
        """
    
        

class Board:
    """The board the players use for the game Twister.
    
    Attributes:
        spinner_colors(list of strings):A list containing all the four possible colors(red,blue,green,yellow,spinner_choice) a player can move to.
        spinner_body_parts(list of strings):A list containing the four possible body parts(left/right hand,left/right foot,spinner_choice) that a player can place on the board
        board (dictionary): Dictionary that represents each circle on the board and whether or not it is occupied.
        player (Player object): A player participating in the game.
        
    """
    
    def __init__(self, board):
        """Initializes a Board object.
        
        Args:
            board (dictionary): Dictionary that represents each circle on the board and whether or not it is occupied.
            
        Side effects:
             Initializes attribute board,spinner_colors,spinner_body_parts
        """
        self.spinner_colors = ["green", "yellow", "blue", "red", "spinner_choice"]
        self.spinner_body_parts = ["right_foot", "left_foot", "right_hand", "left_hand", "spinner_choice"]
        
    def spinner(self,spinner_colors,spinner_body_parts):
        """The spinner randomly selects a body part that the player will move and a color that the player will land on. We will be using a f-string in this method
        
        Args:
            spinner_colors(list of strings):A list containing all the four possible colors(red,blue,green,yellow,spinner_choice) a player can move to.
            spinner_body_parts(list of strings):A list containing the four possible body parts(left/right hand,left/right foot,sinner_choice) that a player can place on the board
            
        Side effects:
            print the value that the spinner gives out. 
            """
            
        color =  random.choice(self.spinner_colors)
       
        if color == self.spinner_colors[4]:
            myinput = input("Enter the color of your choice: ")
            if myinput not in self.spinner_colors:
                raise ValueError("Not a valid color.")
            myinput = input("Enter the color of your choice: ")
            color = myinput
           
        body_part = random.choice(self.spinner_body_parts)
        
        if body_part == self.spinner_body_parts[4]:
            myinput = input("Enter the body part of your choice: ")
            if myinput not in self.spinner_body_parts:
                raise ValueError("Not a valid body part.")
            myinput = input("Enter the body part of your choice: ")
            body_part = myinput
            
        print(f"Move your {body_part} to an open {color} circle")
       
        # return 
        
        
    def elimination(self, player):
        """This method determines when a player loses. We will use a conditional expression within this method.
        
        Args:
            player (Player object): The player who fell and got eliminated.
            
        Side effects:
            Prints "Player lost and Other_Player won."
        """
        
    def board_adjustment(self, player):
        """Keeps track of where the players are on the board. Uses dictionary comprehension.
        
        Args:
            player (Player object): A player participating in the game.
            
        Side effects:
            Adjusts the dictionary board.
        
        
        """
        board={"green1":"open",
               "green2":"open",
               "green3":"open",
               "green4":"open",
               "green5":"open",
               "green6":"open",
               "yellow1":"open",
               "yellow2":"open",
               "yellow3":"open",
               "yellow4":"open",
               "yellow5":"open",
               "yellow6":"open",
               "blue1":"open",
               "blue2":"open",
               "blue3":"open",
               "blue4":"open",
               "blue5":"open",
               "blue6":"open",
               "red1":"open",
               "red2":"open",
               "red3":"open",
               "red4":"open",
               "red5":"open",
               "red6":"open",
                }
        
    def __str__(self):
        """"Returns a representation of the board. We will be using a magic method in this method."""
        

#main function
    
    
    
    
