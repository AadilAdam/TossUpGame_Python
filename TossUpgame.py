#name:    AADIL AHMED ADAM

#date:    10/22/2015

#class:   CS542-02

#PYTHON SOURCE CODE FOR THE DICE GAME- TOSS UP!
#IT ALLOWS TWO PLAYERS TO COMPETE AND
#THE PLAYER WITH THE HIGH SCORE OVER 100 WINS


#PROGRAM

from sys import exit
import random

playerOne=[]       #array to store name of player one
playerTwo=[]       #array to store name of player two
playername=[]      #array to store name of player when required to check which player is playing

#This function is defined take user input of the names of players
def inputnames():
    
    global playerOne
    global playerTwo
    
    playerOne=input('Enter the playerOne name:')
    playerTwo=input('Enter the playerTwo name:')
    print()
    print('Lets toss to check who begins the game!!!')
    #passing the names of both players to toss function
    toss(playername)


#This function is defined to determine which player starts the game
def toss(playername):
    global playerOne
    global playerTwo
    
    #random function generating two values of a toss.
    flip=random.randint(0,1)                            
    print('Toss pick =',flip)
    
    if(flip==0):
        playername=playerOne
        print('Lets begin the game: ',playerOne)
        #pass the player1 name as argument to the roll dice function
        rolldice(playername)                            
    else:
        playername=playerTwo
        print('Lets begin the game: ',playerTwo)
        #pass the name of player2 as argument to the roll dice function
        rolldice(playername)                            



die_colors=['R','Y','Y','G','G','G']                    #declaring an array of die colors


#function defining the rolling of dice function
def rolldice(playername):
    
    global total_score1          #global variable to store the value of total score of player one
    global total_score2          #global variable to store the value of total score of player two
    global turn_score1           #global variable to store the value of turn score of player one
    global turn_score2           #global variable to store the value of turn score of player two
    playername
    global numDice               #variable to store the value of total number of dice
    global playerOne
    global playerTwo

    #until the score of both players reach 100, loop
    while(total_score1<100 and total_score2<100):
        
        turn_score1=0
        turn_score2=0
        numDice=10         #total number of dice
        dice=[]            #array to store the output of dice roll
        
        #random function to generate the values of dice roll with dice=10
        for die in range(0,numDice):
            dice.append(die_colors[random.randint(0,5)])
        print('displaying the output of the dice roll function:-')
        print(dice,sep=" ")
        print()
        green=dice.count('G')                  #counting the number of greens in the dice list
        print('The number of greens in this turn: ',green)
        print()
        
        if(playername==playerOne):    
            turn_score1=turn_score1+green
            print('The turn score of playerOne : ',turn_score1)
            roll_remdice(numDice,green,playerOne)
            total_score1=total_score1+turn_score1
            print('The total score of playerOne : ',total_score1)
            print('---------------------------------------------------------')
            print()
            playername=playerTwo
        
        else:
            turn_score2=turn_score2 + green
            print('The Turn score of playerTwo ',turn_score2)
            print()
            roll_remdice(numDice,green,playerTwo)
            total_score2=total_score2+turn_score2
            print('The total score of playerTwo ',total_score2)
            print('---------------------------------------------------------')
            print()
            playername=playerOne

    #if total score of any player >= 100, give a chance to other player to roll once
    if(total_score1>=100):
        roll_remdice(10,0,playerTwo)
        total_score2=total_score2+turn_score2
    else:
        roll_remdice(10,0,playerOne)
        total_score1=total_score1+turn_score1


#this function is defined to roll the remaining dice after the main roll function
def roll_remdice(numDice,green,playername):
    
    global turn_score1
    global turn_score2
    global total_score1
    global total_score2
    
    global playerOne
    global playerTwo
    global yellow
    
    turn_is_over=0
    numDice
    playername
    dice1=[]

    while(not turn_is_over):
        dice1=[]
        print("Do you want to roll again?")
        player_input=input('roll or quit-')
        
        if(player_input=='roll'):
            remDice=numDice-green
            if (remDice == 0):		# if no more dice to roll, then reset to 10
                remDice = 10
                numDice = 10
            print('The remaining dice to roll in this turn is  ', remDice)
            
            for die in range(0,remDice):
                dice1.append(die_colors[random.randint(0,5)])
                
            print('displaying the output of the dice roll function:-')
            print(dice1,sep = " ")
            print()
            
            #counting the dice colors in this roll
            green=dice1.count('G')
            yellow=dice1.count('Y')
            red=dice1.count('R')
            print('The number of greens is this turn is : ', green)

            #condition checking the number of greens to decide to continue or quit
            if(green>=1):
                if(playername==playerOne):
                    turn_score1= turn_score1+green
                    print('The turn score of playerOne is : ',turn_score1)
                    print()
                    numDice=remDice
                else:
                    turn_score2=turn_score2+green
                    print('The turn score of playerTwo',turn_score2)
                    print()
                    numDice=remDice
                        
            elif(red>0):
                print('The number of red is' , red)
                print("\nRED LIGHT. Lose points for this turn.\n")
                turn_is_over = 1
                
                if(playername==playerOne):
                    turn_score1=0
                    print('The turn score of playerOne is:' , turn_score1)
                    print()
                else:
                    turn_score2=0
                    print('The turn score of playerTwo is ', turn_score2)
                    print()

            else:           #all dice colors is yellow
                numDice=remDice

                    
        else:
            turn_is_over=1
            if(playername==playerOne):
                print('The total turn score of playerOne',turn_score1)
                print('---------------------------------------------------------')
                print()
            else:
                print('The total turn Score of playerTwo',turn_score2)
                print('---------------------------------------------------------')
                print()

    


total_score1=0
total_score2=0
turn_score1=0
green=0             #number of green
yellow=0            #number of yellow
turn_score2=0
numDice=10
remDice=0           #To store the value of remaining dice to roll
dice=[]

print ("Welcome to the Toss UP! dice game \n")
print('*********************************************************')
print('A player begins  the game by rolling all 10 dice. \n Each die has one red side, two yellow sides, and three green sides.\n')
print('player gets points for each die that lands on green \n and scores a 0 if he/she encounters a red with no green \n')
print('you can quit your turn whenever you want to, returning control to other player \n')
print('***********************************************************')
print('Be the player with the highest score over 100 at the end of the game.\n')
print('---------------------------------------------------------')
input("Press enter to begin the game.")
    
inputnames()

print('The total score of player1 is \n', total_score1)
print('The total score of player2 is \n', total_score2)
print('---------------------------------------------------------')
    
if(total_score1>total_score2):
    print('Yeahhhhhh!!!! Congratulations playerOne  ', playerOne)
    print()
    print('Well played and good luck next time  ', playerTwo)
    print('---------------------------------------------------------')
else:
    print('Yeahhhhhhhh!!!!! Congratulations playerTwo  ', playerTwo)
    print()
    print('Well played and good luck next time  ', playerOne)

print('end of the Toss Up! game \n')

