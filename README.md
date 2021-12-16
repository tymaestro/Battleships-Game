# Battleships Game
<br>
ADD SCREENSHOT
<br>
<br>
Battleships is a strategy guessing game that can be played against the computer or between two players. This version will be played against the computer

Battleships is accessible to, and can be enjoyable, for all age groups but requires a good strategy to be played well. Anyone who loves a challenege will enjoy this game

## How to play
<br>
This version of Battleships will be played on two 6x6 grids. One for the player and one for the computer

The aim of the game is to sink all of the opponent's battleships before they sink all of yours

At the start of the game you will be asked to input your name

Then, you will input your co-ordinates (row followed by column) and press enter to check if you have hit one of the computer's ships

Depending on the result, both your board and the computer's board will be updated with the position of your respective guesses

This will repeat until there is a winner!


## Features
<br>






<br>
<br>

### Main heading




<br>
<br>


<br>
<br>




<br>
<br>

### Main Game Section




<br>
<br>


<br>
<br>


<br>
<br>


<br>
<br>


<br>
<br>


### Features Left To Implement

Implement a feature to give the player the option of choosing the position of their ships instead of having them positioned at random

Add the option of choosing a player vs player setup where you can play against your friends instead of playing the computer

## Technologies

Python

[Github](https://github.com/) was used for version control to store commit history

[Heroku](https://www.heroku.com/home) was used to deploy our final project


## Testing
<br>

### Validator Testing

PYTHON: No errors were returned when passing through the official Pep8online linter

<img src="./docs/pep8-screenshot.png">

### Bugs

#### Solved Bugs
<br>

### Remaining Bugs
<br>


<hr>
<br>

<br>
<br>

### Feature Function

Testing has been done using both [PythonTutor](https://pythontutor.com/visualize.html#mode=edit) and print() to verify and debug my code

This is the random module that has been imported for use in generating random numbers for board creation and computer guess

<img src="./docs/random-module.png">

Testing create_board()

<img src="./docs/create-board-function.png">

Testing print_board()

<img src="./docs/print-board-function.png">

Testing welcome()

<img src="./docs/welcome-function.png">

Testing ship_placement()

<img src="./docs/ship-placement-function.png">

Testing start_game()

<img src="./docs/start-game-function.png">

<br>
<br>
All functions within my run.py file have been tested throughout this project using print() and PythonTutor to ensure that each function executed as intended.
<br>
<br>
An example of testing done within PythonTutor to verify correct execution of my random number 'for' loop
<br>

<br>
<br>


## Deployment

The site was deployed to the Heroku app through the following steps:
<br>
<br>
1. Ensure that any unnecessary imports (such as import pprint) are deleted before deployment
<br>
<br>
2. Ensure that any input methods used have a new line (\n) at the end of the text due to quirk in the software used to create the mock terminal
<br>
<br>
3. Ensure that any dependencies are added to the requirements.txt file using pip3 freeze > requirements.txt in the terminal. This will update the requirements.txt file
<br>
<br>
4. Create a free Heroku account. Heroku will ask for basic details such as name, email, and role (student)
<br>
<br>
5. Confirm your account by clicking on the confirmation link sent via email
<br>
<br>
6. Create your password and proceed
<br>
<br>
7. Accept terms of service
<br>
<br>
8. Create a new app for your project
<br>
<br>
9. Choose a unique name for your app (non-unique names are not allowed on Heroku)
<br>
<br>
10. Choose your location (USA or Europe) then create the app
<br>
<br>
11. Once the app has been created, click the settings tab in the upper right of the screen
<br>
<br>
12. Add a Config Var based on instructions from Code Institute
<br>
<br>
13. The value for key within Config Var is ‘PORT’ and the value for value is 8000
<br>
<br>
14. If you have used a file on your project that deals with sensitive information, make sure to add this as a Config Var as well. For example, a CREDS.json file would use CREDS as the value for key and the contents of the CREDS.json file as the value
<br>
<br>
15. Add these Config Vars to your app
<br>
<br>
16. Next step is to add two Buildpacks to your app
<br>
<br>
17. These Buildpacks are Python and nodejs. It is very important to ensure that they are in the order of the Python buildpack first, followed by the nodejs buildpack
<br>
<br>
18. Scroll to the top of the page and click the deploy section
<br>
<br>
19. Choose Github as the deployment method
<br>
<br>
20. Scroll down and confirm that we want to connect to Github
<br>
<br>
21. Search for repository name within Github. My project is named “battleships-game22”
<br>
<br>
22. Click the connect button to the right of the screen
<br>
<br>
23. Scroll down, ensure that you have selected the main (master) branch, and click on deploy branch under the Manual Deploy heading
<br>
<br>
24. This will allow you to see the deployment logs as it runs
<br>
<br>
25. Once this process has finished, there will be a message that confirms that the app has been successfully deployed
<br>
<br>
26. At the bottom of the screen, there will be a button to view the deployed project in the mock terminal
<br>
<br>
27. Click the button to view the project

<br>
<br>
The live link can be found here - 

## Credits
<br>

Code institute for the deployment terminal and general README structure

[Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)) for a general overview of Battleships and how to play

Part of my testing was done using [PythonTutor](https://pythontutor.com/visualize.html#mode=edit)



## Acknowledgements

Thank you to my mentor who gave me very helpful feedback and was very encouraging during our mentor sessions.

Also, a big thank you to the Slack community over the course of this entire module.