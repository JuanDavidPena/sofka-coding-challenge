# sofka-coding-challenge
## Overview
In this challenge we are going to create a simple contest of questions and answers. We are going to design a solution that allows to have and modify a database of questions (`questionsDB.py`) with four options and one single correct answer. We are going to have diferent levels of dificulty and that dificulty is going to increase when the player answers correctly. Also, as the player answers correctly he will be accumulating prizes.

## How to use
In order to use the game, first you will have to clone this repository to your local machine
`Your local machine or environment must hae Python3 installed!`
Use `python3 --version` to verify this.
After you have the repository, now move to the main directory using `cd sofka-coding-challenge`

Now you just have to execute `python3 app.py` and enjoy the game!

Make sure you have permission to write in this directory in order to save your score files.

## Playing
First you will be asked for your name, after that you will see the questions and four options to answer.
You have to type the letter of the option that you think is correct!
Also you can type "retire" whenever you want to keep the prizes you have collected and walk away.

## Saving
When you type "yes" to save your score, a file will be created with the name of the player that is currently playing and a json string containing the name and the score will be saved.

## Authors
Juan David Peña
