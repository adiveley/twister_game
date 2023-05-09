""""A twister game written in python that allows multiple people to play twister"""
import random



class Player:
    """One of the people playing the game
    
    Attributes:
        d"""
        
    
    
    def __init__(self,position,name,board):
        """Initializes a person object. Uses optional parameters.
        
        Args:
            name(str): the name of the player
            
        Side effects: 
            Initializes attribute name,right_foot,left_foot,right_hand,left_hand
        """        
       
        self.position=position
        self.name=name
        self.board=board
        self.status = "safe"
    
    def turn(self):
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

        # Instance of board to the player 
        # 
        body_part,color=self.board.spinner()
        
        
        print(f"{self.name} move your {body_part} to an open {color} circle.")
       
        # number=input("Enter a number 1-6 to represent the position of the color you want to move to.")
        # number = int(number)
        # if number<1 or number>6:
        #     raise ValueError("You did not enter a valid number")
        # else:
        #     number = str(number)
        #     color_position =color+number 
            
        
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
        self.board.board_adjustment(old_position,new_position)
        
          
            
    def __str__(self):
         """Returns a representation of where the players are. We will be using a magic method in this method."""
         return (f"{self.name}'s current position is {self.position}.")


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
        
        print("green1 yellow1 blue1 red1 \ngreen2 yellow2 blue2 red2 \ngreen3 yellow3 blue3 red3 \ngreen4 yellow4 blue4 red4 \ngreen5 yellow5 blue5 red5 \ngreen6 yellow6 blue6 red6")
        
    def __str__(self):
        g1 = self.board["green1"]
        g2 = self.board["green2"] 
        g3 = self.board["green3"]
        g4 = self.board["green4"]
        g5 = self.board["green5"]
        g6 = self.board["green6"]
        y1 = self.board["yellow1"]
        y2 = self.board["yellow2"]
        y3 = self.board["yellow3"]
        y4 = self.board["yellow4"]
        y5 = self.board["yellow5"]
        y6 = self.board["yellow6"]
        b1 = self.board["blue1"]
        b2 = self.board["blue2"]
        b3 = self.board["blue3"]
        b4 = self.board["blue4"]
        b5 = self.board["blue5"]
        b6 = self.board["blue6"]
        r1 = self.board["red1"]
        r2 = self.board["red2"]
        r3 = self.board["red3"]
        r4 = self.board["red4"]
        r5 = self.board["red5"]
        r6 = self.board["red6"]
        green="green"
        red="red"
        blue="blue"
        yellow="yellow"
        return print(f"{green} {yellow} {blue} {red}\n{g1} {y1} {b1} {r1}\n{g2} {y2} {b2} {r2}\n{g3} {y3} {b3} {r3}\n{g4} {y4} {b4} {r4}\n{g5} {y5} {b5} {r5}\n{g6} {y6} {b6} {r6}\n")
        
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
         # Change spinner into a function so that we o not have to call an instance of board   
        
        self.color =  random.choice(self.spinner_colors)
       
        if self.color == self.spinner_colors[4]:
            myinput = input("Enter the color of your choice: ")
            if myinput not in self.spinner_colors:
                raise ValueError("Not a valid color.")
           # myinput = input("Enter the color of your choice: ")
            self.color = myinput
           
        self.body_part = random.choice(self.spinner_body_parts)
        
        if self.body_part == self.spinner_body_parts[4]:
            myinput = input("Enter the body part of your choice (right_foot, left_foot, right_hand, left_hand): ")
            if myinput not in self.spinner_body_parts:
                raise ValueError("Not a valid body part.")
            #myinput = input("Enter the body part of your choice: ")
            self.body_part = myinput
            
        
        return self.body_part, self.color
       
        
        
        
    def elimination(self,old_position,new_position,player):
        """This method determines when a player loses. We will use a conditional expression within this method.
        ## Comments: pass in the player instance here as an arg
        ex) player
        Side effects:
            Prints "Player lost and Other_Player won."
        """
        print(player)
        max_feet = 3
        max_hands = 2
        
        
        vertical_coordinate_old, horizontal_coordinate_old = self.coordinates[old_position]
        vertical_coordinate, horizontal_coordinate = self.coordinates[new_position]
        
        abs_expression_horiz = abs(horizontal_coordinate - horizontal_coordinate_old) # will come back to this
        abs_expression_vert = abs(vertical_coordinate - vertical_coordinate_old)
        

        #test = Player(, name1, self)
        
        if old_position == "":
                  pass
        else:
            if new_position== "right_hand" or new_position == "left_hand":
                   player.status = "eliminated" if abs_expression_horiz > max_hands or abs_expression_vert > max_hands else "safe"  
                   # player.status
            else:
                player.status = "eliminated" if abs_expression_horiz > max_feet or abs_expression_vert > max_feet else "safe"  
            
        if player.status == "eliminated":
            print(f"{player.name} has been eliminated. ")
        
                #Your new position is {dictionary}
                
    def board_adjustment(self,old_position,new_position):
        """Keeps track of where the players are on the board. 
        
        Args:
            player (Player object): A player participating in the game.
            
        Side effects:
            Adjusts the dictionary board.
        
        """
                
        #dictionary = {key: test.position[key] == "" for key in test.player1_current_position if test.status == "eliminated"}
        
      

        self.board[old_position]="open"
        self.board[new_position]="closed"

        
        
        
        
        
        
        
        

def main():
    #Uses custom class composition.
    boardcall = Board()
    name1 = input("Enter player1 name: ")
    name2 = input("Enter player2 name: ")
    player1_current_position = {"right_foot":"blue1", "left_foot":"yellow1", "right_hand":"", "left_hand":""}
    player2_current_position = {"right_foot":"blue6","left_foot":"yellow6", "right_hand":"", "left_hand":""}
        
    
    player1= Player(player1_current_position,name1,boardcall)
    player2=Player(player2_current_position,name2,boardcall)
    
    
    
    while player1.status=="safe" and player2.status=="safe":
        player1.turn()
        player2.turn()
        # if player1.status=="eliminate" and player2.status=="safe":
        #     print(f"{name2} has won the game")
        # else:
        #     if player1.status=="safe" and player2.status=="eliminate":
        #         print(f"{name1} has won the game")
                    
        
        
        
# we will be using composition for htis method
    

if __name__ == "__main__":
    main()
