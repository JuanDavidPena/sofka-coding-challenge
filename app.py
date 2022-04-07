from tracemalloc import stop
from Question import Question
from Player import Player
from Encoder import Encoder
from questionsDB import get_question
from random import random, randrange
import json

# Array to store the prizes, so they are easy to modify
balance = [0, 100, 1000, 10000, 100000, 1000000]

def intro_question(lvl):
    """ Generates a random introduction to the new question """
    lvl += 1
    bal = balance[lvl]
    v = [0 for i in range(5)]
    v[0] = "Here is question #%s worth $%s." % (lvl, bal)
    v[1] = "We're going to question #%s for you to win $%s." % (lvl, bal)
    v[2] = "Question #%s for $%s now." % (lvl, bal)
    v[3] = "This is the turn of question #%s that will get you $%s." % (lvl, bal)
    v[4] = "Now it is the turn of question #%s. Win $%s!" % (lvl, bal)

    n = randrange(5)
    return v[n] + "\n"


def save_score(player):
    """Saves the json string of the Player class into a file with the player's name"""
    with open(player.name, "w") as f:
        json.dump(Encoder().encode(player), f)
    print ("Thank you so much for playing %s! We have saved your score."%(player.name))


def handle_retire(player):
    """Handles the prizes when retire and asks the player to save the progress"""
    prize = balance[player.prize]
    print ("So, you are not a risky person huh? \n\
        it is OK! you were incredible %s! \n\
        You answered %s questions right and you won...\n\
        %s !!!!\n\n"%(player.name, player.prize, prize))
    save = input("Would you like to save your score?(yes/no) ")
    if save == "yes":
        save_score(player) 
    else:
        print ("Thank you for playing %s!\n"%(player.name))


def handle_win(player):
    """Handles the prizes when all questions are answered
       and asks the player to save the win"""
    prize = balance[player.prize]
    print ("CONGRATULATIONS! You've made it! \n\
        Amazing performance! %s! \n\
        You answered %s questions right and you won...\n\
        %s !!!!\n\n"%(player.name, player.prize, prize))
    save = input("Would you like to save your score?(yes/no) ")
    if save == "yes":
        save_score(player) 
    else:
        print ("Thank you for playing %s!\n"%(player.name))


def run_quiz(player):
    """Executes the quiz for the respective player"""
    streak = 1
    lvl = 0

    while(streak and lvl < 5):
        random = randrange(10)
        print(intro_question(lvl))
        qDB = get_question(lvl, random)
        question = Question(qDB)
        answer = input(question.get_full_prompt())
        if answer == "retire":
            handle_retire(player)
            streak=0
        else:
            check = question.check_answer(answer)
            if check == True:
                print ("\n-------------You got it %s!-------------\n\n"%(player.name))
                lvl += 1
                player.prize += 1
            else:
                print ("\n-----Oof! I think that is wrong %s!-----\n\n"%(player.name))
                print ("Nevertheless you did great!\n")
                save = input("Would you like to save your score?(yes/no) ")
                if save == "yes":
                    save_score(player)
                else:
                    print ("Thank you for playing %s!\n"%(player.name))

                streak = 0
    if lvl == 5:
        handle_win(player)
    else:
        exit

# Welcome message and asks for the player name to create it and execute the quiz
print (" Welcome to the Softka Quiz Challenge! \n")
name = input(" What is your name? ")

print ("\n Let's start the game, %s! There will be 5 questions\n\
 that are arranged by difficulty. Simplier questions\n\
 go first and are worth less. Every question will have four \n\
 answer choices, of which only one is correct. Answering the hardest,\n\
 5th question, will make you a winner of $1,000,000! \n\
 You can always answer 'retire'to leave with your prize! \n\n\
 So, let's get started!\n"% (name))

player = Player(name)
run_quiz(player)
