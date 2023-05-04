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
        self.player1_current_position = [["right_foot", "blue1"], ["left_foot", "yellow1"], ["right_hand", ""], ["left_hand", ""]]
        self.player2_current_position = [["right_foot", "blue6"], ["left_foot", "yellow6"], ["right_hand", ""], ["left_hand", ""]]
        self.player1 = player1
        self.player2 = player2
        self.spinner_colors = ["green", "yellow", "blue", "red", "spinner_choice"]
        self.spinner_body_parts = ["right_foot", "left_foot", "right_hand", "left_hand", "spinner_choice"]

        self.player1_status = "safe"
        self.player2_status = "safe"
        
    def turn(self, player):
        """Executes a player turn. Uses f string and sequence unpacking.
        
        Args:
            player(str): Name of the current player
        Raises:
            ValueError: User did not type color or body part.
        Side effects:
            Prompts the current player to spin for a body part and a color.
            Prints {self.player} move your {spin.body_part} to an open {spin.color} circle.
        """
        # We need to append the current position for wherever the player is moving to. Havwe the player choose a number to reresent
        # were they are moving to 
        
        print (self)
        
        turn_spin = input("Type 'spin' to spin the spinner: ")
        if turn_spin != "spin":
            raise ValueError("You must type spin to spin the spinner.")
    
        spin = Board()
        spin.spinner()
        
        print(f"{self.player1} move your {spin.body_part} to an open {spin.color} circle.")
       
        number=input("Enter a number 1-6 to represent the position of the color you want to move to.")
        number = int(number)
        if number<1 or number>6:
            raise ValueError("You did not enter a valid number")
        else:
            number = str(number)
            color_position = spin.color+number 
            
        
        while spin.board[color_position]== "closed":
            print("This position is already closed please choose somewhere another number.")
            number=input("Enter a number 1-6 to represent the position of the color you want to move to.") 
            number = int(number)
            if number<1 or number>6:
                raise ValueError("You did not enter a valid number")
            else:
                number = str(number)
                color_position = spin.color+number 
        
        
        for body_parts,position_colors in self.player1_current_position:
            empty_list=[]
            if spin.spinner_body_parts=="right_foot":
                old_position=self.player1_current_position.pop(0)
                empty_list.append("right_foot")
                empty_list.append(color_position)
                self.player1_current_position[0]=empty_list
            if spin.spinner_body_parts=="left_foot":
                old_position=self.player1_current_position.pop(1)
                empty_list.append("left_foot")
                empty_list.append(color_position)
                self.player1_current_position[1]=empty_list
            if spin.spinner_body_parts=="right_hand":
                old_position=self.player1_current_position.pop(2)
                empty_list.append("right_hand")
                empty_list.append(color_position)
                self.player1_current_position[2]=empty_list
            if spin.spinner_body_parts=="left_hand":
                old_position=self.player1_current_position.pop(3)
                empty_list.append("left_hand")
                empty_list.append(color_position)
                self.player1_current_position[3]=empty_list
                
        spin.elimination()
        spin.board_adjustment()
        
            
            
    def __str__(self):
        """"Returns a representation of where the players are. We will be using a magic method in this method."""
        return (f"{self.player1}'s current position is {self.player1_current_position[0]}, {self.player1_current_position[1]}, {self.player1_current_position[2]}, {self.player1_current_position[3]}. \n{self.player2}'s current position is {self.player2_current_position[0]}, {self.player2_current_position[1]}, {self.player2_current_position[2]}, {self.player2_current_position[3]}")


class Board:
    """The board the players use for the game Twister.
    
    Attributes:
        spinner_colors(list of strings):A list containing all the four possible colors(red,blue,green,yellow,spinner_choice) a player can move to.
        spinner_body_parts(list of strings):A list containing the four possible body parts(left/right hand,left/right foot,spinner_choice) that a player can place on the board
        board (dictionary): Dictionary that represents each circle on the board and whether or not it is occupied.
        player (Player object): A player participating in the game.
        
    """
    
    def __init__(self):
        """Initializes a Board object.
        
        Args:
            board (dictionary): Dictionary that represents each circle on the board and whether or not it is occupied.
            
        Side effects:
             Initializes attribute board,spinner_colors,spinner_body_parts
        """
        self.spinner_colors = ["green", "yellow", "blue", "red", "spinner_choice"]
        self.spinner_body_parts = ["right_foot", "left_foot", "right_hand", "left_hand", "spinner_choice"]
        self.color = ""
        self.body_part = ""
        
        self.position = {"green1":[1,4],
               "green2":[2,4],
               "green3":[3,4],
               "green4": [4,4],
               "green5":[5,4],
               "green6":[6,4],
               "yellow1":[1,3],
               "yellow2":[2,3],
               "yellow3":[3,3],
               "yellow4":[4,3],
               "yellow5":[5,3],
               "yellow6":[6,3],
               "blue1":[1,2],
               "blue2":[2,2],
               "blue3":[3,2],
               "blue4":[4,2],
               "blue5":[5,2],
               "blue6":[6,2],
               "red1":[1,1],
               "red2":[2,1],
               "red3":[3,1],
               "red4":[4,1],
               "red5":[5,1],
               "red6":[6,1],
                }
        
        self.board = {
               "green1":"open",
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
        
        print("green1 yellow1 blue1 red1 \ngreen2 yellow2 blue2 red2 \ngreen3 yellow3 blue3 red3 \ngreen4 yellow4 blue4 red4 \ngreen5 yellow5 blue5 red5 \ngreen6 yellow6 blue6 red6")
        
    def spinner(self):
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
            
        
        self.color =  random.choice(self.spinner_colors)
       
        if self.color == self.spinner_colors[4]:
            myinput = input("Enter the color of your choice: ")
            if myinput not in self.spinner_colors:
                raise ValueError("Not a valid color.")
            myinput = input("Enter the color of your choice: ")
            self.color = myinput
           
        self.body_part = random.choice(self.spinner_body_parts)
        
        if self.body_part == self.spinner_body_parts[4]:
            myinput = input("Enter the body part of your choice (right_foot, left_foot, right_hand, left_hand): ")
            if myinput not in self.spinner_body_parts:
                raise ValueError("Not a valid body part.")
            #myinput = input("Enter the body part of your choice: ")
            self.body_part = myinput
            
        
        return self.body_part, self.color
       
        
        
        
    def elimination(self):
        """This method determines when a player loses. We will use a conditional expression within this method.
        
        
            
        Side effects:
            Prints "Player lost and Other_Player won."
        """
        
        player = Players()
        
        max_feet = 3
        max_hands = 2
        
        #{key: abs(value[1] - player.old_position[-1]) for value in self.position if player.player1_current_position[2:]}
        
        for key, value in self.position:
            abs_expression_horiz = abs(value[1] - player.old_position[-1]) # will come back to this
            abs_expression_vert = abs(value[0] - player.old_position[-1])

        
        for x in player.player1_current_position:
            if player.player1_current_position[2:]:
                player.player1_status = "eliminated" if abs_expression_horiz > max_hands or abs_expression_vert > max_hands else "safe"       
            else:
                player.player1_status = "eliminated" if abs_expression_horiz > max_feet or abs_expression_vert > max_feet else "safe"  
                
                
    def board_adjustment(self):
        """Keeps track of where the players are on the board. Uses custom class composition.
        
        Args:
            player (Player object): A player participating in the game.
            
        Side effects:
            Adjusts the dictionary board.
        
        """
        
        player=Players()
        player.turn()
        self.board[player.color_position]="closed"
        self.board[player.old_position]="open"
            
    
        

def main():
    
    player1 = input("name: ")
    player2 = input("name: ")
    players = [player1, player2]
    
    playercall = Players(player1, player2)
    boardcall = Board()
    
    while playercall.player1_status == "safe" and playercall.player2_status == "safe":
        for player in players:
            #players[0].turn
            playercall.turn(player1)
            playercall.turn(player2)
        
        
        
        
# we will be using composition for htis method
    

if __name__ == "__main__":
    main()
