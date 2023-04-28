""""A twister game written in python that allows multiple people to play twister"""
import random

class Players:
    """One of the people playing the game
    
    Attributes:
        name(str): The name of the player
        right_foot(int): A number(1) that represents the right foot
        left_foot(int): A number(2) that represents the left foot
        right_hand(int): A number(3) that represents the right hand
        left_hand(int): A number(4) that represents the left hand"""
        
    
    
    def __init__(self, player1, player2):
        """Initializes a person object. Uses optional parameters.
        
        Args:
            name(str): the name of the player
            
        Side effects: 
            Initializes attribute name,right_foot,left_foot,right_hand,left_hand
        """
        self.player1_current_position = [("right_foot", "blue1"), ("left_foot", "yellow1"), ("right_hand", ""), ("left_hand", "")]
        self.player2_current_position = [("right_foot", "blue6"), ("left_foot", "yellow6"), ("right_hand", ""), ("left_hand", "")]
        self.player1 = player1
        self.player2 = player2
        #player1.left_foot = 
        #player1.right_foot = 
        #player2.left_foot = 
        #player2.right_foot = 
        
        self.spinner_colors = ["green", "yellow", "blue", "red", "spinner_choice"]
        self.spinner_body_parts = ["right_foot", "left_foot", "right_hand", "left_hand", "spinner_choice"]
        
    def turn(self, player):
        """Executes a player turn. Uses f string.
        
        Args:
            player(str): Name of the current player
        Raises:
            ValueError: User did not type color or body part.
        Side effects:
            Prompts the current player to spin for a body part and a color.
            Prints {self.player} move your {spin.body_part} to an open {spin.color} circle.
        """
        
        body_part = input("Type 'body part' to spin for a body part: ")
        if body_part != "body part":
            raise ValueError("You must type body part.")
       
        color = input("Type 'color' to spin for a color: ")
        
        if color != "color":
            raise ValueError("You must type color.")
        
        spin = Board()
        spin.spinner()
        
        print(f"{self.player} move your {spin.body_part} to an open {spin.color} circle.")
        
        
    
        

class Board:
    """The board the players use for the game Twister.
    
    Attributes:
        spinner_colors(list of strings):A list containing all the four possible colors(red,blue,green,yellow,spinner_choice) a player can move to.
        spinner_body_parts(list of strings):A list containing the four possible body parts(left/right hand,left/right foot,spinner_choice) that a player can place on the board
        board (dictionary): Dictionary that represents each circle on the board and whether or not it is occupied.
        player (Player object): A player participating in the game.
        
    """
    
    def __init__(self, board, position):
        """Initializes a Board object.
        
        Args:
            board (dictionary): Dictionary that represents each circle on the board and whether or not it is occupied.
            
        Side effects:
             Initializes attribute board,spinner_colors,spinner_body_parts
        """
        self.spinner_colors = ["green", "yellow", "blue", "red", "spinner_choice"]
        self.spinner_body_parts = ["right_foot", "left_foot", "right_hand", "left_hand", "spinner_choice"]
        
        self.position = {"green1":(1,4),
               "green2":(2,4),
               "green3":(3,4),
               "green4": (4,4),
               "green5":(5,4),
               "green6":(6,4),
               "yellow1":(1,3),
               "yellow2":(2,3),
               "yellow3":(3,3),
               "yellow4":(4,3),
               "yellow5":(5,3),
               "yellow6":(6,3),
               "blue1":(1,2),
               "blue2":(2,2),
               "blue3":(3,2),
               "blue4":(4,2),
               "blue5":(5,2),
               "blue6":(6,2),
               "red1":(1,1),
               "red2":(2,1),
               "red3":(3,1),
               "red4":(4,1),
               "red5":(5,1),
               "red6":(6,1),
                }
        
    def spinner(self,spinner_colors, spinner_body_parts):
        """The spinner randomly selects a body part that the player will move and a color that the player will land on. Sequence unpacking and list comprehension.
        
        Args:
            spinner_colors(list of strings):A list containing all the four possible colors(red,blue,green,yellow,spinner_choice) a player can move to.
            spinner_body_parts(list of strings):A list containing the four possible body parts(left/right hand,left/right foot,sinner_choice) that a player can place on the board
            
        Raises:
            ValueError: body part and color selected are not found within the spinnner_color or spinner_body_parts
         
        Returns:
            body_part (str): The body part that the spinner landed on or spinner's choice.
            color (str): The color that the spinner landed on or spinner's choice.
            
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
            
        player = Players()
        
        ([(player.player1_current_position.remove(player1_current_position[0]) and player.player1_current_position.append((body_part, color))) 
          for player.body_part, player.color in  player.player1_current_position if body_part == "right_foot"])
        ([(player.player1_current_position.remove(player1_current_position[1]) and player.player1_current_position.append((body_part, color))) 
          for player.body_part, player.color in  player.player1_current_position if body_part == "left_foot"])
        ([(player.player1_current_position.remove(player1_current_position[2]) and player.player1_current_position.append((body_part, color))) 
          for player.body_part, player.color in  player.player1_current_position if body_part == "right_hand"])
        ([(player.player1_current_position.remove(player1_current_position[3]) and player.player1_current_position.append((body_part, color))) 
          for player.body_part, player.color in  player.player1_current_position if body_part == "left_hand"])
        
        return body_part, color
       
        
        
        
    def elimination(self, status):
        """This method determines when a player loses. We will use a conditional expression within this method.
        
        Args:
            status(str): whether the player is safe or eliminated
            
        Side effects:
            Prints "Player lost and Other_Player won."
        """
        status = ""
        player = Players()
        
        max_feet = 3
        max_hands = 2
        
        for key,value in self.position:
            abs_expression_horiz = abs(value[1] - ___)
            abs_expression_vert = abs(value[0] - ___)
            status = "eliminated" if abs_expression > max_feet else "safe"

            
        for player.player1_current_position[2:] in :
            abs_expression = 
            status = "eliminated" if abs_expression > max_hands else "safe"        
        
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
               "yellow1":"closed",
               "yellow2":"open",
               "yellow3":"open",
               "yellow4":"open",
               "yellow5":"open",
               "yellow6":"closed",
               "blue1":"closed",
               "blue2":"open",
               "blue3":"open",
               "blue4":"open",
               "blue5":"open",
               "blue6":"closed",
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
# call spinner
    
    
    
    
