#these lines help import things from the Python library into the code. 
import json
import pgzrun
from random import randint 
from pgzero.actor import Actor
import pygame
import time

#this line is for the width of the game display screen
WIDTH = 700
#this line is for the height of the game display screen
HEIGHT = 600
#this line tells the code where the dots should be placed on the game display screen based on the height
DOT_MAX_HEIGHT = 400

#this line tells the code to open the file "QuizList.json" which is a seperate file.
quizListFile = open("QuizList.json")
#this line tells the code to read the file "QuizList.json" when the file has been opened up. 
quizListFileContent = quizListFile.read()
#this line parses a valid JSON string and converts it into a Python List.
#each item in the list contains multiple key value pairs.
#the keys are questions, answer, choices, and level. 
#the item choices contains multiple key value pairs. 
quizList = json.loads(quizListFileContent)

#dots contains what the image and position should be for all of the dots on the screen
dots = []
#each line contains coordinates for where the line should be once two dots are clicked
lines = []
#if a dot is clicked then next_dot_clicked will change its value +1
next_dot_clicked = 0
#if a dot is clicked then next_dot will have the value of next_dot_clicked minus 1
next_dot = 0

#0 to 14 is the range of values of the dots in the game
for dot in range(0, 14):
    #this line will create a new Actor using the image of the dot in the images folder
    actor = Actor("dot")
    #this will ensure that the dots appear at least 20 pixels away from the edge of the screen so the whole dot is shown. 
    actor.pos = randint(20, DOT_MAX_HEIGHT - 20), \
    randint(20, DOT_MAX_HEIGHT - 20)
# this will add a new item to the list, which the item is actor, the actor represents the dots on the screen. 
    dots.append(actor)
#defines the function draw 
def draw():
    global next_dot_clicked
    # this sets the background color to black 
    screen.fill("black")
    # this creates a variable to keep track of the current number label
    number = 1 
    #all the lines in the for loop draw each dot on the screen along the number label
    for dot in dots:
        screen.draw.text(str(number), \
                        (dot.pos[0], dot.pos[1] + 12))
        #this executes the code that will draw the dots out 
        dot.draw()
        #the value of the number of a dot is increased by 1 when a new one is drawn on the screen
        number = number + 1 
    #this line of code below in the for loop wil draw the lines on the screen
    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0, 0))
# this if statement checks the value of a dot, and if the value of the dot is greater than 0, than it will display a question that is selected from the quizList which matches the value of the dot clicked by the user.
    if next_dot_clicked != 0:
        # this line draws the question selected from the quizList list based on the value of a dot that the user has clicked on.
        quiz = quizList[next_dot_clicked - 1]
        screen.draw.text(quiz["question"], \
                        (20, 500), color="white")
        y = 520
        #this is what draws the words on the screen, and what the text size should be, font, color, and position on the screen. 
        for letter, text in quiz["choices"].items():
            screen.draw.text(("{} ({})".format(letter, text)), (20, y), color="white")
            y += 20
        #this allows only a portion of the game screen to be updated, instead of the entire screen. 
        pygame.display.flip()
        #this waits for the user's input for the question and if its true. 
        waitForInput = True
        #executes the code below while the code above is waiting for the user's input.
        while waitForInput:
            #the for loop below executes event in pygame.event.get
            for event in pygame.event.get():
                #if event.type equals pygame.KEYDOWN then the code below will be executed
                if event.type == pygame.KEYDOWN:
                    #if the user's answer matches the correct answer of the question, then correct will be drawn on the screen
                    if event.unicode.lower() == quiz["answer"].lower():
                        screen.draw.text("Correct", (20, 480), color="green")
                        #if the user finishes all of the questions correctly, than You Win will be drawn on the screen
                        if next_dot_clicked == 13:
                            screen.draw.text("YOU WIN", (200, 300), color="green", fontsize=100)
                        pygame.display.flip()
                    #if the user does not answer a question correctly, then You Lose will be drawn on the screen. 
                    else:
                        screen.draw.text("YOU LOSE", (200, 300), color="red", fontsize=100)
                        pygame.display.flip()
                        #then, the game will automatically exit and end the game for the user
                        time.sleep(5)
                        pygame.quit()
                        exit()
                    #the input will be false if the user's answer is wrong for the question. 9- 
                    waitForInput = False

        #this line of code is the value of the variable next_dot_clicked when the user has not clicked another dot besides the first one
        next_dot_clicked = 0

#the line of code in the def function is to let the function change the values of the global variables next_dot and lines.
def on_mouse_down(pos):
    global next_dot
    global lines
    global next_dot_clicked 
    #this line checks if the player has clicked on the next dot in the sequence.
    if dots[next_dot].collidepoint(pos):
        #this line checks if the player has already clicked on the first dot.
        if next_dot:
            #this draws a line betweeen the current dot and the previous one
            lines.append((dots[next_dot -1].pos, dots[next_dot].pos))
            next_dot_clicked = next_dot
        #this sets next_dot to the next number
        next_dot = next_dot + 1
    #the lines below set the next_dot back to the first dot and deletes all the lines if the player clicks on the wrong dot on the screen.
    else:
        lines = []
        next_dot_clicked = 0
        next_dot = 0
    
def on_key_down(key):
    if key == keys.ESCAPE:
        pygame.quit()
        exit()

pgzrun.go()
