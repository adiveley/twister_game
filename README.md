# twister_game
INST326 Final Project - Twister multiplayer board game created using Python

# Explanation of the files in our repository
The README.md file explains how to run our game while also explaining the purpose of each file found on github. It also tells which of us wrote which methods or functions and tells which technique we had demonstrated in these methods.
The twister_game.py file contains our code for this projects. Using this file anyone is capable of running this code.

# Instructions on how to run the program from the command line
To run the program from the command line we call python(python3) twister_game.py

# How to use our program. 
After running the program on the command the program will ask the user for their name. Following the name the program will ask the user to type spin. If the spinner lands on spinner choice for colors it will prompt the user to enter a color(red,green,blue, or yellow). If the spinner lands on spinner choice for the body parts you will be asked to enter a body part(right_hand,left_hand,right_foot,or left_foot). If the spinner does not land on spinner choice the program will provide you with a color to move to and a body part to move. After you get the color and body part you will be asked to enter a number from 1 to 6. These numbers represents the position of the color on the board. 

The player is only allowed to move three spaces horizontally or vertically when moving a foot. If the player is moving a hand they are only allowed to move 2 spaces horizontally or vertically. If this condition is violated the player will be eliminated. If player one is eliminated the other player will still have to spin for that turn since they have not went yet. If one player is eliminated and one has won it will print who is eliminated and who has won. If both players lose during the turn then the program will print that both players have lost and end the program. Each turn the program will print the state of the board. It will show the current position that are available and not available. Those that are available will be open and those that are occupied will show closed. If a player is eliminated the program will also remove their body parts from the board and change their position from closed to open. This will be represented by a print statement that prints an empty string representing that the body parts are not on the board.

# Attribution
| Method/Function       | Primary Author |    Techniques demonstrated                   |
| ----------------------|----------------|----------------------------------------------|
| Player.__init__       |Emmanuel Leonard| Composition of two custom classes            |
| Player.turn           |Emmanuel Leonard|f-string                                      |
| Player.__str__        |Allison Diveley |magic method                                  |
| Board.spinner         | Tyler Dulin    |Nothing                                       |
|Board.elimination      | Tyler Dulin    |Sequence unpacking and conditional expression |
|Board.board_adjustment |Allison Diveley |Dictionary Comprehension                      |
