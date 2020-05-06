import time
import libdw.sm as sm

class Player:
##  Created so that it is easier to obtain and modify player data
    
    def __init__(self, name, nric, age, score = 0):
        if len(name) == 0:
            self.name= "newplayer"
        else:
            self.name = name.capitalize()
        self.nric = nric.title()
        self.age = age
        self.score = score
        
    def get_details(self):
        return "Name:\t{}\nNRIC:\t{}\nAge:\t{}".format(self.name, self.nric, self.age)

    def set_details(self, word):
        if len(word) == 0:
            self.name= "newplayer"
        elif word.isdigit():
            self.age = word
        elif word[1].isdigit():
            self.nric = word.title()
        else:
            self.name = word.title()

    details = property(get_details, set_details)

##------------------------------------------------------------------------------------
class CoronaQuiz(sm.SM):
##  This is the main class
##  Incorporated SM to enable interchangability between states (Initial, Game, End)
##  SM acts as the frame of the game, allowing player to see scoreboard, play , replay or quit game    
    
    start_state = "Initial State"
    
    def get_next_values(self, state, inp):

        if state == "Initial State":
            if inp == "P" or inp == "R":
                output = "\n------Please key in your details below------"
                print(output)
                next_state = "Game State"
                
            elif inp == "Q":
                output = "Thank you for your time!"
                print(output)
                next_state = "End State"

            elif inp == "S":
                self.seescores()
                output = input("Enter P to play, S to see scoreboard, or Q to quit: ").capitalize()
                next_state = state
                
            else:
                output = input("Invalid entry. Please enter either P or Q: ").capitalize()
                next_state = state
                
##  Created various methods to segment the game for easier debugging
##  "Game state" is also made simple by implementing more methods for the operation             
        elif state == "Game State": 
            player = self.playerdetails()   ## To acquire player details to be stored in scoreboard
            self.countdown()                ## Countdown timer implemented to prompt the player towards the start of game
            self.questions(player)          ## This is the quiz itself
            self.scoreboard(player)         ## This is to write the results into the scoreboard
            dec = self.decision()           ## Prompts the user if he/she wants to replay, see scoreboard or quit
            output = dec
            if dec == "R" or dec == "S":
                next_state = "Initial State"
            else:
                next_state = "End State"

        return next_state, output

    def playerdetails(self):
        ## Get details of user with error mitigated to a certain extent
        name = input("Please enter your name: ")
        while name.isdigit():
            name = input("Names do not have numbers. Please enter your name again: ")
        nric = input("Please enter your nric: ")
        while nric.isalpha() or nric.isdigit() or len(nric) != 9 :
            nric = input("Input is invalid. Please enter your Nric again: ")
        age = input("Please enter your age: ")
        while not age.isdigit() or len(age) > 2:
            age = input("Age must be in numbers less than 100(eg. 23). Please enter your Age again: ")
        
        player = Player(name, nric, age) ## Instantiate Player class
                            
        while True:                
            answer = input("\n{}\nDo you want to confirm the details (yes/no)? ".format(player.details)).lower()
            if answer == "yes":
                break
            elif answer == "no":
                num_choice = input("1. Name 2. Nric 3. Age\nPlease select the number of the category that you want to change: ")
                if num_choice == "1":
                    change = input("Name: ")
                    while change.isdigit():
                        change = input("Names do not have numbers. Please enter your name again: ")

                elif num_choice == "2":
                    change = input("NRIC: ")
                    while change.isalpha() or change.isdigit() or len(change) != 9 :
                        change = input("Input is invalid. Please enter your Nric again: ")
                    
                elif num_choice == "3":
                    change = input("Age: ")
                    while not change.isdigit() or len(change) > 2:
                        change = input("Age must be in numbers less than 100(eg. 23). Please enter your Age again: ")

                    
                else:
                    print("Invalid answer. Try again")
                player.details = change
            else: 
                print("Please enter either yes or no")
        return player
    
    def countdown(self):
        sec = 3
        while sec >0:
            print("!-!-!-!-!-!-!-!-!-!-!-[{}]-!-!-!-!-!-!-!-!-!-!-!".format(sec))
            sec -= 1
            time.sleep(1)

    def questions(self,player):
        ## Algorithim for quiz
        ## Gets quiz questions from questionbank textfile
        ## Compares input answers with answers in answerbank textfile
        ## Displays correct answer for user
        ## Displayed number of correct answers, time taken and tabulated score
        ## Score is based on time and number of correct answers
        ## Points rewarded for questions increases per question linearly
        print("------Let's go!!! The time has started!-------")
        start_time = time.time()
        qb = open("questionbank.txt", "r")
        ab = open("answerbank.txt", "r")
        ansdata = ab.read()
        qnsdata = qb.read()
        ans_list = ansdata.split("\n")
        qns_list = qnsdata.split("\n")
        times = len(qns_list)
        count = 0
        correct = 0
        for num in range(14):
            linecount=0
            for line in range(count,times+1):
                if qns_list[line] == "":
                    linecount+=1
                    break
                else:
                    print(qns_list[line])
                    linecount+=1
            count+=linecount
            ans = input(">>> ")
            if ans == ans_list[num]:
                print("<<< You got it right! Great job! >>>\n")
                player.score+=(num+1)
                correct+=1
            else:
                print("<<< Aww maan :( The answer is actually {} >>>\n".format(ans_list[num]))
        end_time = time.time()
        time_taken = end_time - start_time
        print("You took {:.1f} secs and got {} correct.".format(time_taken, correct))
        player.score = player.score/time_taken*100
        print("Your total score is {:.1f}".format(player.score))
        ab.close()
        qb.close()
    
    def scoreboard(self, player):
        ## Open in access mode to be able to append results
        if len(player.name) >= 8: ## If else statement implemented for formatting the alignment of name into the scoreboard 
            with open("scoreboard.txt", "a") as f: ## Closes file automatically
                f.write("\n{}\t{}\t{}\t{:.1f}".format(player.name,player.nric,player.age,player.score))
        else:
            with open("scoreboard.txt", "a") as f: 
                f.write("\n{}\t\t{}\t{}\t{:.1f}".format(player.name,player.nric,player.age,player.score))

    def seescores(self):
        ## Implemented partial censoring of NRIC so that other players will not be able to see the full NRIC
        print("-------------------SCOREBOARD-------------------")
        with open("scoreboard.txt", "r") as file:
            print(file.readline())
            for lines in file:
                charlist = []
                for char in lines:
                    if char.isdigit() and len(charlist)<=3:
                        charlist.append(char)
                string = "{}{}{}{}".format(charlist[0],charlist[1],charlist[2],charlist[3])
                print(lines.replace(string ,"****"))
    
        print("-------------------------------------------------")

    def decision(self):
        ## To prompt user on whether to replay, see scoreboard, or quit game
        dec = input("\nEnter R to replay, S to see scoreboard, or Q to quit: ").capitalize()
        #print(dec)
        if dec == "R" or dec == "Q" or dec == "S":
            return dec
        else:
            print("You have entered an invalid response!")
            return self.decision() ## Used recursion to loop and return decision made

    def run(self):
        ## This is to start and keep the SM running
        self.start()
        print("Think you know about the COVID-19 Virus well?\nSee how fast you can complete Corona-Quiz!\n")
        answer = input("Enter P to play, S to see scoreboard, or Q to quit: ").capitalize()
        while True: ## while loop is used so that the SM will always run after it has started, unless "End State" is achieved
            if self.state != "End State":
                new_inp = self.step(answer)
                answer = new_inp
                #print(new_inp)
            else: ## Breaks out of endless loop when "End State" is achieved
                break
        print("----------The game has been terminated----------")
        
CQ = CoronaQuiz() ## Instantiation 
CQ.run() ## Calls for run method in the object instance quizeria
