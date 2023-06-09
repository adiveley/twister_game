""""A twister game written in python that allows multiple people to play twister"""
import random



class Player:
    """A player that is playing the game
    
    Attributes:
        position(dictionary): A dictionary containg the cureent position of the player
        name(string): The name of the people playing the game
        board(custom class composotion): An instance of the board class within the player
        status(string): The current status of the player. Determines if player is safe or eliminated
        
                """
        
    
    
    def __init__(self,position,name,board):
        """Initializes a person object.Uses custom class composition (1/6)
           Author:Emmanuel Leonard
        
        Args:
            position(dictionary): A dictionary containg the cureent position of the player
            name(string): The name of the people playing the game
            board(custom class composotion): An instance of the board class within the player
            
        Side effects: 
            Initializes attribute position, name and board and status
        """        
       
        self.position=position
        self.name=name
        self.board=board
        self.status = "safe"
    
    def turn(self):
        """Executes a player turn. Uses f-string (2/6).
           Author: Emmanuel Leonard
        
        Side effects:
            Prompts the current player to spin for a body part and a color.
            Prints {self.player} move your {spin.body_part} to an open {spin.color} circle.
            Ask the usder to Type 'spin' to spin the spinner: 
            Prints you must type spin to spin the player
            Ask the user to input a number 1-6
            Prints you did not enter a valid number(prints under certain conditions).
            Prints This position is already closed please choose another number
            Changes the attribute self.position.
            Prints the string magic method
        """
        
        print (self)
        
        while True:
            turn_spin = input("Type 'spin' to spin the spinner: ")
            if turn_spin != "spin":
                print ("You must type spin to spin the spinner.")
            else:
                break

        


        body_part,color=self.board.spinner()
        
        
        print(f"{self.name} move your {body_part} to an open {color} circle.")
       
            
        
        while True:
            number=input("Enter a number 1-6 to represent the position of the color you want to move to: ") 
            number = int(number)
            
            if number<1 or number>6:
                print("You did not enter a valid number")
                continue
            else:
                new_position =f"{color}{number}" 
            if self.board.board[new_position]=="closed":
                print("This position is already closed please choose another number. ")
            else:
                break
            
        old_position = self.position[body_part]
        self.position[body_part] = new_position
    
        
        self.board.elimination(old_position,new_position,self)
        self.board.board_adjustment(old_position,new_position,self)
        
          
            
    def __str__(self):
        """ Uses magic method (3/6)
        Author: Allison Diveley
        Returns a representation of where the players are. We will be using a magic method in this method."""
        return (f"\n{self.name}'s current position is {self.position}.\n")


class Board:
    """The board the players use for the game Twister.
    
    Attributes:
        spinner_colors(list of strings):A list containing all the four possible colors(red,blue,green,yellow,spinner_choice) a player can move to.
        spinner_body_parts(list of strings):A list containing the four possible body parts(left/right hand,left/right foot,spinner_choice) that a player can place on the board
        board (dictionary): Dictionary that represents each circle on the board and whether or not it is occupied.
        color(string): color given by the spinner or chosen by the player
        body_part(string):Body part given by the spinner or chosen by the player.
        coordinates(dictionary): Gives the cordinates of each circle on the board.
        
    """
    
    def __init__(self):
        """Initializes a Board object.
           Author: Emmanuel Leonard
           
        Side effects:
             Initializes attribute board,coordinates,spinner_colors,spinner_body_parts,color,body_part
             prints a portrayal of the board. 
        """
        self.spinner_colors = ["green", "yellow", "blue", "red", "spinner_choice"]
        self.spinner_body_parts = ["right_foot", "left_foot", "right_hand", "left_hand", "spinner_choice"]
        self.color = ""
        self.body_part = ""
        
        self.coordinates = {"green1":[1,4],
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
               "": [0,0]
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
        
        print("green1 yellow1 blue1 red1 \ngreen2 yellow2 blue2 red2 \n"
              "green3 yellow3 blue3 red3 \ngreen4 yellow4 blue4 red4 \n"
              "green5 yellow5 blue5 red5 \ngreen6 yellow6 blue6 red6 \n")
        
    
        
    def spinner(self):
        """The spinner randomly selects a body part that the player will move 
        and a color that the player will land on. 
        Author: Tyler Dulin
        
                
        Returns:
            body_part (str): The body part that the spinner landed on or 
            spinner's choice.
            color (str): The color that the spinner landed on or spinner's 
            choice.
        Side effects:
            Alters the attributes color and body_part.
            Ask the player to input a color of their choice(when on spinner choice).
            Ask the player to input a body_part of their choice(when on spinner choice)
            Prints not a valid color or body_part if user does not type the current input
            
            """  


        self.color =  random.choice(self.spinner_colors)
       
        if self.color == self.spinner_colors[4]:
            while True:
                myinput = input("Enter the color of your choice: ")
                if myinput not in self.spinner_colors:
                    print ("Not a valid color.")
                else:
                    break
                
            
                
            self.color = myinput
            
           
            
           
        self.body_part = random.choice(self.spinner_body_parts)
        
        if self.body_part == self.spinner_body_parts[4]:
            while True:
                myinput = input("Enter the body part of your choice "
                        "(right_foot, left_foot, right_hand, left_hand): ")
                if myinput not in self.spinner_body_parts:
                    print("Not a valid body part.")
                else:
                    break
            
            self.body_part = myinput

            
        
        return self.body_part, self.color
       
        
        
        
    def elimination(self,old_position,new_position,player):
        """This method determines when a player loses. We will use a conditional
        expression and sequence unpacking (5/6) within this method.
        Author:Tyler Dulin
        
        Side effects:
            Prints "Player lost."
            Prints the string magic method
            Updates the player.status attribute
        """
        print(player)
        max_feet = 3
        max_hands = 2
        
        
        vertical_coordinate_old, horizontal_coordinate_old = self.coordinates[old_position]
        vertical_coordinate, horizontal_coordinate = self.coordinates[new_position]
        
        abs_expression_horiz = abs(horizontal_coordinate - horizontal_coordinate_old) # will come back to this
        abs_expression_vert = abs(vertical_coordinate - vertical_coordinate_old)
        
        
        if old_position == "":
                  pass
        else:
            if new_position== "right_hand" or new_position == "left_hand":
                   player.status = "eliminated" if abs_expression_horiz > max_hands or abs_expression_vert > max_hands else "safe"  
            else:
                player.status = "eliminated" if abs_expression_horiz > max_feet or abs_expression_vert > max_feet else "safe"  
            
        if player.status == "eliminated":
            print(f"{player.name} has been eliminated. \n")
        
        
                
    def board_adjustment(self,old_position,new_position,player):
        """Keeps track of where the players are on the board. We will use 
        dictionary comprehension (6/6) within this method.
        Author: Allison Diveley
        
        Args:
            player (Player object): A player participating in the game.
            old_position(string): Previous position of a single body part that is found on the board. Ex:green1
            new_position(string): Players current position of a single body part that is found on the board. Ex:yellow6
            
        Side effects:
            Adjusts the board atttribute.
            Prints the name of the player that has lost as well as the current position of their body parts.
        
        """
              
        remove_player = {key: "" for key in player.position if player.status == "eliminated"}
        if player.status == "eliminated":
            print (f'{player.name} has been removed from the board: {remove_player}\n') 
      
      
        if player.status=="safe":                
            self.board[old_position]="open"
            self.board[new_position]="closed"
            

        
        if player.status=="eliminated":
            self.board[player.position["right_foot"]]="open"
            self.board[player.position["left_foot"]]="open"
            self.board[player.position["right_hand"]]="open"
            self.board[player.position["left_hand"]]="open"



            

def main():
    """Runs the program using the turn method
       Author: Allison Diveley
       
       Side effects:
        Asks the user to input their name.
        Prints the current state of the board using the board attribute.
        Prints who has won the game. 
        Prints if both players have lost the game. 
    
    """
    
    
    
    
     
    boardcall = Board()
    name1 = input("Enter player1 name: ")
    name2 = input("Enter player2 name: ")
    player1_current_position = {"right_foot":"blue1", "left_foot":"yellow1", "right_hand":"", "left_hand":""}
    player2_current_position = {"right_foot":"blue6","left_foot":"yellow6", "right_hand":"", "left_hand":""}
        
    
    player1= Player(player1_current_position,name1,boardcall)
    player2=Player(player2_current_position,name2,boardcall)
    
    
    
    
    while player1.status=="safe" and player2.status=="safe":
        player1.turn()
        print(f'Here is the current state of the board: {boardcall.board}')
        player2.turn()
        print(f'Here is the current state of the board: {boardcall.board}')
    if player1.status=="eliminated" and player2.status=="safe":
             print(f"\n{name2} has won the game")
    else:
        if player1.status=="safe" and player2.status=="eliminated":
            print(f"\n{name1} has won the game")
        else:
            if player1.status=="eliminated" and player2.status=="eliminated":
                print(f"Both {name1} and {name2} have lost the game")
    
        
    

    

if __name__ == "__main__":
    main()