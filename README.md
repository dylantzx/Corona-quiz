# Corona-Quiz
***
Corona Quiz is a quiz about COVID-19. It is created to test people's knowledge on the basic information of COVID-19 in Singapore, and provides the player with insightful knowledge about what and what not to do. 
## Prerequisites

To be able to run the game, the library libdw has to be installed and can be done so using [pip](https://pip.pypa.io/en/stable/) on the terminal.
```
pip install libdw
```
The user will also be required to extract the following textfiles provided in the zip file into the same folder: 

* questionbank.txt
* answerbank.txt
* scoreboard.txt

## How to play the game
***
When the code has started, simply enter P to play, S to see the scores on the scoreboard or Q to quit.

When P is entered, the player will be prompted to key in his Name, Nric and Age. The player will then be prompted again to confirm the details and is able to change the them. 

*Note: These details are meant for identification of the players in the context where this is a game created by the government, with incentives given to the top 3 players.*

Once the player has confirmed his/her details by typing "yes", a 3 seconds countdown will start and the quiz will begin.

The quiz consists of 14 questions and the player who achieves the highest number of correct answers in the shortest time will obtain a higher score. The scoring is set such that every following question will give higher and higher points. For example, question 1 gives 1 point, question 2 gives 2 points etc. Each question has options a,b,c, etc. and where multiple answers are possible for a question, for example, if (a) and (b) are the answers, simply type and enter a,b .

The correct answer will also be displayed below the answer entered by the user, and the user will be able to review his/her answers after the quiz.

At the end of the quiz, the user will then be given a choice to replay, look at the scoreboard, or quit the game, by entering R, S or Q respectively.

## Code description
***
The quiz is coded using Object-Oriented Programming with only 2 distinct classes, the Player class and the CoronaQuiz class.

The Player class is created so that the player's information can be stored and obtained easily. It is also created for easier classification and recognizability of the code. It consists of 3 methods, the \__init__ method, getter method and the setter method. A property function is also used to make the code backward compatible.

The CoronaQuiz class, the main class, is also an SM class that comprises of a few methods namely:
* get_next_values
* playerdetails
* countdown
* questions
* scoreboard
* seescores
* decision
* run 

The SM class is created to toggle between states, so that the functionality of starting the game, restarting the game, quiting the game and looking at the scoreboard, can be easily implemented and modified through the *get_next_values* method. For this game, there are only 3 states, namely the *Initial state*, *Game state* and *End state*, where the "Game State" is kept as compact and simple as possible through the use of various methods.

The purpose of the methods are self-explanatory through the names, where:
1) *playerdetails* - Get player details (Name, NRIC, age)
2) *countdown* - 3 seconds countdown to prep the user
3) *questions* - The question-answer portion of the quiz
4) *scoreboard* - store player's information into scoreboard after the quiz has ended
5) *seescores* - Enable the user to see the scores by displaying the scoreboard
6) *decision* - Ask for the user's decision on replaying, looking at the scoreboard or quiting the game
7) *run* - This is the most important code, which is to start the SM class and keep it running as long as the state is not at *End State*

## Video
---
<https://www.youtube.com/watch?v=MJsNlWUfQvM&feature=youtu.be>








